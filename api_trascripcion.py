from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
nltk.download('punkt')

app = Flask(__name__)

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
    transcript_video= YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
    text_lines = [line['text']
                   for line in transcript_video]
    text = ' '.join(text_lines)
    sentences = nltk.sent_tokenize(text)

    # Segmentar las oraciones en pasos de la receta
    recipe_steps = []
    for sentence in sentences:
        if any(char.isdigit() for char in sentence):
            recipe_steps.append(sentence)

    return jsonify({'transcription': recipe_steps})


app.run(debug=True)
    
    





