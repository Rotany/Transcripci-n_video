from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize

import re
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

    # Limpiar el texto de cualquier HTML
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()

    #Elimina caracteres no deseados
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Reemplazar múltiples espacios por un solo espacio
    clean_text = re.sub(r'\[.*?\]', '', clean_text)  # Eliminar contenido entre corchetes (e.g., [ Aplausos ])

    # Tokenización de oraciones
    sentences = sent_tokenize(clean_text)

     #Segmentar las oraciones en pasos de la receta
    recipe_steps = []
    current_step = ""
    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in ["primero", "luego", "después", "finalmente"]) or any(char.isdigit() for char in sentence):
            if current_step:
                recipe_steps.append(current_step.strip())
            current_step = sentence
        else:
            current_step += " " + sentence
    if current_step:
        recipe_steps.append(current_step.strip())
        
    return jsonify({'transcription':recipe_steps})


app.run(debug=True)
    
    





