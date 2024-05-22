from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
from utils import limpiar_text
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

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
    transcript_video = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
    text_lines = [line['text']
                   for line in transcript_video]
    text = ' '.join(text_lines)
    sentences = limpiar_text(text)

    return jsonify({'transcription':sentences})

if __name__ == '__main__':
    app.run(debug=True)
    
    





