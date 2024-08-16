# Transcripción de Videos de YouTube para convertirlos en Blogs de Recetas de Cocina.

## Este proyecto es una API basada en Flask que permite transcribir videos de YouTube a texto, anonimizar el contenido y generar un blog de recetas de cocina con un formato HTML a partir de la transcripción. Luego almacena y gestiona las transcripciones en una base de datos PostgreSQL.

## Requisitos:

## - Python 3
## - PostgreSQL
## - Flask**
## - OpenAI API Key: La clave de la API de OpenAI para llamar a GPT.
## - Dependencias: Ver `requirements.txt`

# Funcionalidad:

## Transcripción de Videos de YouTube: A partir del ID de un video de YouTube, la API descarga el contenido del video y lo transcribe a texto utilizando una biblioteca de procesamiento de videos de YouTube.

## Anonimización del Contenido: Usando la API de OpenAI (ChatGPT), el título del video y la transcripción completa son procesados para ser anonimizados, es decir, se eliminan o reemplazan datos personales o identificadores que puedan estar presentes.

## Generación Automática de Blogs en HTML: La transcripción anonimizada es luego convertida a un formato HTML listo para ser usado en un blog de recetas de cocina. Esto incluye no solo el texto, sino también metadescripciones optimizadas para SEO y una estructura de URI amigable para la web.

## Eliminación de Transcripciones: La API permite crear nuevas transcripciones, leer todas las transcripciones almacenadas, y eliminar transcripciones específicas de la base de datos PostgreSQL.

# Estructura del proyecto
# transcripcion-youtube-recetas/
## api_transcripcion.py   Archivo principal de la aplicación Flask
## models.py              Definición de los modelos de base de datos
## openai_utils.py        Funciones para interactuar con la API de OpenAI
## utils.py               Utilidades para generar HTML y manipular texto
## requirements.txt       Dependencias del proyecto
## README.md              Este archivo
