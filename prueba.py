#import nltk 
#nltk.download("punkt")
#from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import re
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from flask_cors import CORS, cross_origin
from flask import jsonify, request,Flask



#loader = YoutubeLoader.from_youtube_url('https://www.youtube.com/watch?v=4oeJmwXQ-Ng', add_video_info= True, language = ['es'])
#print(loader)
from langchain_community.document_loaders import YoutubeLoader

# Crea una instancia del YoutubeLoader con el ID del video
video_id = "4oeJmwXQ-Ng"
loader = YoutubeLoader(video_id, add_video_info= True, language= ['es'])

# Carga el contenido del video
transcripcion = loader.load()

# Muestra el contenido del video

#print(f"video de: {transcripcion[0].metadata['author']}")
print(f"Titulo: {transcripcion[0].metadata['title']}")
print("")
print(transcripcion[0].page_content)
llm = OpenAI(temperature = 0)
print(llm)
