import os
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import re
nltk.download('punkt')
import unicodedata 
import re


def limpiar_text(text):    
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()
    clean_text = re.sub(r'\s+', ' ', clean_text)  
    clean_text = re.sub(r'\[.*?\]', '', clean_text)  
    print(clean_text)
    print("^^^^^^^^^^^^^^^^^^^^^^^^")
    return sent_tokenize(clean_text)

def construir_uri(title):
    title = unicodedata.normalize('NFD', title)     # Normaliza el título para descomponer caracteres Unicode.
    title = ''.join(c for c in title if unicodedata.category(c) != 'Mn')    # Elimina los diacríticos de los caracteres.
    title = title.lower()
    title = re.sub(r'[^a-z0-9\-]', '-', title)     # Reemplaza caracteres no permitidos con guiones.
    title = re.sub(r'-+', '-', title)     # Remplaza múltiples guiones consecutivos en uno solo.
    title = title.strip('-')     # Limpia los guiones al inicio y al final del título.
    return title


def generate_html_from_json(json_data):
    with open('template.html', 'r', encoding='utf-8') as f:
        template_html = f.read()
    
    blog_uri = json_data["uri"]
    blog_title = json_data["title"]
    blog_meta_description = json_data["meta_description"]

    html_content = template_html.replace('"""title"""', f'<title>{blog_title}</title>')
    html_content = html_content.replace('"""body"""', json_data['html_content'])
    html_content = html_content.replace('"""description"""', f'<meta name="description" content="{blog_meta_description}">')
    html_content = html_content.replace("```html", "").replace("```", "")

    output_filename = f'{blog_uri}.html'

    if os.path.exists(output_filename):
        return None
    else:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        return blog_title