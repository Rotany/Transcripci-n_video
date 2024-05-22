import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import re
nltk.download('punkt')


# Limpiar el texto de cualquier HTML
def limpiar_text(text):    
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()

    #Elimina caracteres no deseados
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Reemplazar múltiples espacios por un solo espacio
    clean_text = re.sub(r'\[.*?\]', '', clean_text)  # Eliminar contenido entre corchetes (e.g., [ Aplausos ])

    # Tokenización de oraciones
    return sent_tokenize(clean_text)



