import openai

seo_keyword = " 'receta de rechupete' según convenga."
system_content_create_html_from_transcription = (
    "Eres un experto en crear archivos html a partir de texto. Quiero que conviertas 'todo el texto' que te voy a pasar en un archivo html. De hecho solo quiero que me pases el contenido del body.", 
    "No quiero justificacion de lo que me has hecho solo quiero que me pases directamente el html. ",
    "No quiero que me crees unicamente un solo div con un solo parrafo. ",
    "El texto que te voy a pasar siempre va estar relacionado con cocina. ",
    "Me gustaria que tuviera varios div y varis parrafos, si puedes añadir tambien una lista de ingredientes siempre que lo mencione, la lista de ingredientes colocalo primero, después del titulo. ",
    f"La palabra clave que voy a posicionar en el seo quiero que sea {seo_keyword}, asi que repitelea varias veces y ponloa siempre y cuando tenga sentido. ",
    "Quiero también que posiciones otras palabras en función de la receta de la que este hablando la transcripción.",
    "Siempre añade en el HTML el 'body'."
)

system_content_anonymize_transcription = (
    "Eres un experto en anonimizar transcripciones. He conseguido transcripciones de diversas personas de plataformas de video, especialmente YouTube. ",
    "No quiero tener ningún problema legal, así que necesito que anonimices el texto de las transcripciones. Para ello, por favor omite las introducciones, frases de bienvenida y cualquier palabra o frase que no esté relacionada directamente con el contenido del video. ",
    "Por ejemplo, elimina frases como 'bienvenidos a mi canal' , 'en la cocina de [nombre]' o 'no olvides de suscribirte a mi canal' o 'suscribete a mi canal'. ",
    "Además, modifica el texto para que no sea idéntico al del video. Puedes añadir contenido nuevo o eliminar partes, siempre respetando la esencia del contenido, que trata sobre cocina o recetas de cocina. ",
    "Tu respuesta debe ser únicamente el texto ya anonimizado, sin explicaciones adicionales ni comentarios. Gracias."
)

system_content_anonymize_titulo = (
    "Eres un experto en anonimizar transcripciones. He conseguido transcripciones de diferentes personas de plataformas de video especialmente YouTube. ",
    "No quiero tener ningun problema legal, así que necesito que anonimices el 'Title' del texto de las transcripciones. Para ello, por favor omite los titulos que contengan el nombre del canal, o cualquier otro nombre solo quiero el nombre de la receta.",
    "Por ejemplo, elimina frases como Sopa de Camaron |'Rosita' o 'kwa."
    "Además, modifica el titulo para que no sea idéntico al del video. Puedes añadir contenido nuevo o eliminar partes, siempre respetando la esencia del contenido, que trata sobre cocina o recetas de cocina. ",
    "Tu respuesta debe ser únicamente el titulo ya anonimizado, sin explicaciones adicionales ni comentarios. Gracias."
)


def call_chatgpt(cleaned_text:str, system_content, model="gpt-3.5-turbo", temperature=0):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": str(system_content)},
            {"role": "user", "content": cleaned_text}
        ],
        temperature=temperature
    )
    contenido_html = response.choices[0].message.content
    return contenido_html
