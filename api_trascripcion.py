from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
from utils import limpiar_text, construir_uri
from flask_cors import CORS, cross_origin
#from langchain_community.llms import openai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain
from models import YoutubeTranscription, db
import os
from datetime import datetime
import openai

openai.api_key=os.environ['OPENAI_KEY']
#client = OpenAI(api_key=openai_api_key)

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@localhost:5432/{os.environ["DB_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

# Create the tables within the app context
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Transcripción de Videos de YouTube</h1>
<p>API para transcribir videos de YouTube a texto utilizando el ID del video.</p>'''

@app.route('/api/v1/transcribe', methods=['POST'])
def transcribe():
    # Obtener el ID del video de YouTube del cuerpo de la petición
    video_id = request.json.get('video_id', None)
    if not video_id:
        return jsonify({'error': 'falta el id_video'})
    
    existing_transcription = YoutubeTranscription.query.get(video_id)
    if existing_transcription:
        pass
        #return jsonify({'error': 'La transcripción ya existe'}), 409
    
    fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    loader= YoutubeLoader(video_id, add_video_info= True, language= ['es'])
    documents = loader.load()
    
    text = ' '.join([doc.page_content for doc in documents])
    title = documents[0].metadata['title'] if 'title' in documents[0].metadata else 'Sin título'
    print(f'Título del video: {title}')
    imagen = documents[0].metadata['thumbnail_url'] if 'thumbnail_url' in documents[0].metadata else None
    
    uri = construir_uri(title)
    cleaned_text = limpiar_text(text)[0]
    system_content = (
        "Eres un experto en crear archivos html a partir de texto. Quiero que conviertas 'todo el texto' que te voy a pasar en un archivo html. De hecho solo quiero que me pases el contenido del body.", 
    "No quiero justificacion de lo que me has hecho solo quiero que me pases directamente el html.",
    "No quiero que me crees unicamente un solo div con un solo parrafo.",
    "El texto que te voy a pasar siempre va estar relacionado con cocina.",
    "Me gustaria que tuviera varios div y varis parrafos, si puedes añadir tambien una lista de ingredientes siempre que lo mencione"
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": str(system_content)},
                {"role": "user", "content": cleaned_text}
            ],
        temperature=0
    )
    
    content_html = response.choices[0].message.content



    transcription = YoutubeTranscription(
        id=video_id, titulo=title, contenido_transcription=cleaned_text,
        imagen=imagen, uri=uri, fecha_inicio=fecha_creacion, contenido_html=content_html
    )
    db.session.add(transcription)
    db.session.commit()
    
    return jsonify({'title': title,'transcription':cleaned_text, 'content_html': content_html})

@app.route("/api/v1/youtube_transcription", methods=['GET'])
def get_youtube_transcription():
    youtube_trascriptions = YoutubeTranscription.query.all()
    lista_vacia = [{'id': t.id, 'title': t.titulo, 'contenido_transcription': t.contenido_transcription} for t in youtube_trascriptions]
    return jsonify({'items': lista_vacia})


@app.route('/api/v1/delete_transcription', methods=['DELETE'])
def delete_transcription():
    # Obtener el ID del video de YouTube del cuerpo de la petición
    video_id = request.json.get('video_id', None)
    if not video_id:
        return jsonify({'error': 'falta el id_video'}), 400
# Verificar si la transcripción existe
    transcription = YoutubeTranscription.query.get(video_id)
    if not transcription:
        return jsonify({'error': 'La transcripción no existe'}), 404
    

    # Eliminar la transcripción
    db.session.delete(transcription)
    db.session.commit()

    return jsonify({'message': 'Transcripción eliminada exitosamente'}), 200
    


                                                                                                                                                                                                                                                                                                                   
                                                  
if __name__ == '__main__':
    app.run(debug=True)
    
    





