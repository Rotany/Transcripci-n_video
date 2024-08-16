from flask import Flask, jsonify, request
from utils import generate_html_from_json, limpiar_text, construir_uri
from flask_cors import CORS, cross_origin
from langchain_community.document_loaders import YoutubeLoader
from models import YoutubeTranscription, db
import os
from datetime import datetime
import openai
from openai_utils import call_chatgpt, system_content_create_html_from_transcription, system_content_anonymize_transcription,system_content_anonymize_titulo,system_content_meta_description

openai.api_key=os.environ['OPENAI_KEY']

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@localhost:5432/{os.environ["DB_NAME"]}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
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
        return jsonify({'error': 'La transcripción ya existe'}), 409
    
    fecha_creacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    loader= YoutubeLoader(video_id, add_video_info= True, language= ['es'])
    documents = loader.load()
    
    text = ' '.join([doc.page_content for doc in documents])
    title = documents[0].metadata['title'] if 'title' in documents[0].metadata else 'Sin título'
    title_anonymized = call_chatgpt(title,system_content_anonymize_titulo)
    
    uri = construir_uri(title_anonymized)
    cleaned_text = limpiar_text(text)[0]
    text_anonymized = call_chatgpt(cleaned_text,system_content_anonymize_transcription,temperature=0.2, model="gpt-4o")
    meta_description = call_chatgpt(text_anonymized, system_content_meta_description)

    content_html = call_chatgpt(text_anonymized, system_content_create_html_from_transcription, model="gpt-4o")


    transcription = YoutubeTranscription(
        id=video_id, titulo=title_anonymized, contenido_transcription=text_anonymized,
        uri=uri, fecha_inicio=fecha_creacion, contenido_html=content_html, meta_description = meta_description
    )
    db.session.add(transcription)
    db.session.commit()
    
    return jsonify({'title': title_anonymized,'transcription':text_anonymized, 'content_html': content_html})

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
    
@app.route('/api/v1/generate_blogs', methods=['POST'])
def generate_blogs():
    youtube_trascriptions = YoutubeTranscription.query.all()
    transcriptions_content = [
        {
            'title': t.titulo,
            "html_content": t.contenido_html,
            "meta_description": t.meta_description,
            "uri": t.uri
            }
        for t in youtube_trascriptions
    ]
    files_created = []
    for data in transcriptions_content:
        filename_created = generate_html_from_json(data)
        if filename_created:
            files_created.append(filename_created)


    return jsonify({
        'message': 'Transcripción pasada a blog',
        'files created': files_created 
        }), 200


    

                                                                                                                                                                                                                                                                                                                   
                                                  
if __name__ == '__main__':
    app.run(debug=True)
    
    





