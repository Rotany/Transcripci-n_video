import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import re
nltk.download('punkt')
import unicodedata 
import re


# Limpiar el texto de cualquier HTML
def limpiar_text(text):    
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()

    #Elimina caracteres no deseados
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Reemplazar múltiples espacios por un solo espacio
    clean_text = re.sub(r'\[.*?\]', '', clean_text)  # Eliminar contenido entre corchetes (e.g., [ Aplausos ])

    # Tokenización de oraciones
    return sent_tokenize(clean_text)

def construir_uri(title):
        title = unicodedata.normalize('NFD', title)
        title= ''.join(c for c in title if unicodedata.category(c) != 'Mn')
        title = title.lower()
        title = re.sub(r'[^a-z0-9\-]', '', title)
        return title



