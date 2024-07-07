import openai


system_content_create_html_from_transcription = (
    "Eres un experto en crear archivos html a partir de texto. Quiero que conviertas 'todo el texto' que te voy a pasar en un archivo html. De hecho solo quiero que me pases el contenido del body.", 
    "No quiero justificacion de lo que me has hecho solo quiero que me pases directamente el html.",
    "No quiero que me crees unicamente un solo div con un solo parrafo.",
    "El texto que te voy a pasar siempre va estar relacionado con cocina.",
    "Me gustaria que tuviera varios div y varis parrafos, si puedes añadir tambien una lista de ingredientes siempre que lo mencione"
)

system_content_anonymize_transcription = (
    "Eres un experto en anonymizar transcripciones, he conseguido transcripciones de x personas de youtube, ",
    "no quiero ningun problema legal, podrias anonimizar el texto para cuando digan cosas como 'bienvenidos a mi canal' o 'en la cocina de x'",
    "has que el texto no sea igual al video, añade contenido nuevo o elimina contenido, pero respetando la esencia del contenido, que sera ",
    "material sobre cocina o recetas de cocina. Solo dame como respuesta el texto ya anonimizado, no me digas nada más, ninguna explicación ni nada."
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
