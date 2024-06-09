from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
from utils import limpiar_text
from flask_cors import CORS, cross_origin
from langchain_community.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import YoutubeLoader
from models import YoutubeTranscription, db
import os

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@localhost:5432/{os.environ["DB_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

# Create the tables within the app context

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
    
    loader= YoutubeLoader(video_id, add_video_info= True, language= ['es'])
    documents = loader.load()
    #for doc in documents:
            #print(doc)
    
    text = ' '.join([doc.page_content for doc in documents])
    title = documents[0].metadata['title'] if 'title' in documents[0].metadata else 'Sin título'
    
    cleaned_text= limpiar_text(text)
    
    return jsonify({'title': title,'transcription':cleaned_text})

if __name__ == '__main__':
    app.run(debug=True)
    
    





