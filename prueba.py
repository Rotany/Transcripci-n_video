import nltk 
nltk.download("punkt")
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import re

#text= ""las tensiones entre España y Argentina han crecido este fin de semana por qué Qué fue lo que pasó qué declaraciones se hicieron polémicas cuéntanos José Antonio López muy buenas noches para tié t Buenas noches Sí el ministro de exteriores de España José Manuel alvárez declaró que el gobierno no descarta romper relaciones con Argentina su presidente Javier Miley No pide disculpas,
        #después de llamar corrupta a la esposa del presidente del gobierno Pedro Sánchez Sánchez precisamente dijo hoy que mi ley no ha estado a la altura y también le ha pedido disculpas públicas el ministro alvárez Enrique convocó ya al embajador de Argentina aquí en España para hablar de este asunto ayer alvárez llamó a consulta cerina la embajadora de España en Argentina lo que supone La retirada temporal de la representante española del país latinoamericano la televisión Argentina entrevistó el ministro del interior de este país Guillermo Francos quien dijo que no habrá disculpas y que mi ley no mencionó nombres el presidente argentino hizo estas declaraciones enri en el acto que el ultraderechista vox realizó ayer en la plaza de toros de la de alegre aquí en Madrid que sirvió para inaugurar la campaña para las elecciones europeas de junio Javier m estuvo el fin de semana aquí en Madrid para acudir al evento ultraderechista no tuvo ningún acto oficial presentó su libro el camino libertario este libro retirado de las librerías por la editorial planeta por mentir le organizaron de último momento un desayuno con empresarios españoles para justificar según la prensa Argentina un viaje que costó al erario de su país ,
#50,000 si te parece vamos a escuchar las polémicas palabras de aquí en Madrid y qué calaña de gente atornillada al poder y Qué niveles de abuso puede llegar a generar digo aú cuando tenga la mujer corrupta digamos ensucia y se tome c días para pensarlo [ Aplausos ] y muy bien José Antonio Gracias y muy buenas noches gracias Saludos Buenas noches [ Música ]""

#def strip_html(text):
    #soup = BeautifulSoup(text, "html.parser")
    #return soup.get_text()

#def remove_between_square_brackets(text):
    #return re.sub('\[[^]]*\]', '', text)


#def denoise_text(text):
    #text = strip_html(text)
    #text = remove_between_square_brackets(text)
    #return text

#cleaned_sample = denoise_text(text)
#sentences= sent_tokenize(cleaned_sample)
#for i, sentence in enumerate(sentences):
    #print(f"Sentence {i+1}: {sentence}")
    
##print(cleaned_sample)
#words = word_tokenize(cleaned_sample)


#print("Tokenized Words:", words)
#print("Tokenized sentences:", sentences)
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import re

# Texto de ejemplo
text = """o no [ Música ] sí [ Música ] buenas cómo están bienvenidos al canal bienvenidos a un nuevo vídeo yo tengo a en el día de hoy vamos a estar haciendo unas albóndigas riquísimas pero cualquier albóndiga van a hacer unas albóndigas ve ganas tremendas bien jugosas bien sabrosas para ponerlas arriba de una buena salsa y unos buenos fideos la receta es muy pero muy simple así que no te la puedes perder por nada del mundo ya sabes que si te gustó el vídeo puedes dejar un pulgar citó para arriba y suscribirte al canal ahora si arranquemos",
        "primero vamos a arrancar hidratando las hojas ponemos dos tazas de soja en un bowl y la cubrimos de agua hirviendo la vamos a dejar reposar durante unos minutos y",
        "luego lo vamos a enjuagar y la vamos a escurrir muy pero muy bien tengo menos de afilador ha decido precorte perejil mientras la soja está ahí hidratándose vamos a picar un puñadito de hojitas de perejil que también puede ser cilantro una cebollita mediana y un pimiento rojo pequeñito esto lo hacen manual o con una picadora [ Música ] ahora que ya tengo todo picadito vamos a enjuagar muy bien esta soja y vamos a quitar todo el agua para que quede lo más séquito posible [ Música ] sobre una sartén vamos a cocinar la cebolla y el morrón acá atrás nos estoy preparando la salsita para estos fideos que es muy simple no es la gran cosa por eso no estoy filmando básicamente use el puré de tomates con una cebollita y listo sobre la sartén ponemos un poquito de aceite y cuando haya tomado un poquito de temperatura agregamos la cebolla y el pimiento condimentamos con un poquito de pimienta negra y un poquito de sal vamos a cocinar esto hasta que estén tiernas las verduras vamos a dar de que las cebollas en tiza poner transparente y ahí ya estaría en este bowl vamos a poner la soja que ya hidratamos el perejil la cebollita y el morrón que ya cocinamos ahora es el turno de las especias que le dan ese saborcito particular a toda esta mezcla ustedes pueden utilizar las especias que decidan poner por lo más básico un poquito de comino pimienta sal orégano o lo que tengan en casa no se limiten yo les voy a mostrar lo que voy a usar en esta ocasión porque me gusta el sabor que aporta debe poner un poquito de ají molido apenas media cucharadita también ajo en polvo le voy a poner media cucharadita y voy a usar bajara que es una mezcla de especias árabes que últimamente lo uso bastante porque me gusta la combinación que tiene al comprarlas ya lista es como que está todo en proporción si yo no quisiera hacer en casa no sé si me saldría pero si no lo tienen no se hagan drama si no quieren tener pueden consultar en casa tienen tienda online con un millón de especias pero está la verdad es que la recomiendo un montón para que tengan una idea esta mezcla tiene nuez moscada pimienta negra coriandro comino clavo de olor canela cardamomo pimentón y chile excelente está muy muy buena y de esto le voy a poner una cucharadita en la cajita de descripción que está acá abajo les voy a dejar el link con la tienda online de casa juan ahora vamos a mezclar todo muy bien le voy a agregar un poquito más de sal y para que todo esto ligue y nos quede bien armadito la albóndiga voy a utilizar harina en este caso harina de garbanzos si no la tienen pueden utilizar harina de avena por ejemplo o pueden utilizar harina de trigo o lo que tengan en su casa vamos a poner unas",
        "4 cucharadas colmadas aproximadamente esto es estimativo porque puede que la preparación de ustedes haya quedado con un poquito más de humedad y requiera un poquito más de harina ahora la manera más fácil de unir todo esto y saber si necesitamos más harina o no es apretando bien con las manos [ Música ] voy a agregar una cucharada más ustedes se van a dar cuenta de que de harina ya están bien cuando agarren la preparación y queda compacta no se desarma de todas maneras no se pasen de rosca con la harina porque ahora esto tiene que descansar en la heladera por lo menos media hora si pueden dejarlo más tiempo mejor o durante toda la noche para que los sabores se mezclen bien y además para que la harina empiece a absorber todos los líquidos y ahí vamos a ver bien la consistencia final que va a tener esta preparación así como está aplasta un poquito y lo vamos a llevar a la heladera ahora vamos a empezar a armar las albóndigas vamos a tomar un poco de la preparación apretamos con nuestras manos para armar la bolita y así de simple tenemos nuestra albóndiga lista la podemos ir apoyando en una placa hasta que terminemos con toda la masa hago este movimiento de ir aplastando para formar la bolita porque si yo hago esto se termina desarmando de esta manera ejerzo presión y queda bien compacta no hace falta girar la en la palma de la mano de última con los dedos terminamos de dar la forma [ Música ] cantidad de albóndigas que salieron en total unas",
        "27 si ustedes no las quieren consumir a todas porque son muchas o les quieren comer",
        "después a esta misma vez y te la pueden llevar al píxel que se congelen y cuando estén duras las ponen en una bolsita que sea apta para el freezer y",
        "después les valls sacando el vídeo quienes van a coma yo ahora voy a cocinarlas no a todas algunas en una sartén y",
        "luego las podemos poner en la salsa así las comemos con los fideos aquí tengo una sartén en el fuego voy a tirar un poquito de aceite y voy a poner las albóndigas [ Música ] las voy a ir girando a medida que se vayan cocinando traten de quedarse al lado de la sartén para que no se les queme en la base una vez que ya están doraditas por todas partes que quedaron selladas esto si quieren lo pueden hacer al horno no hace falta que lo hagan a la plancha una vez que estén así vamos a poner ahora la salsa para que se caliente también y se mezcle con las albóndigas con el sellado que hicimos de estas albóndigas más allá de cocinarlas porque se tenía que cocinar la harina de garbanzos lo que permite es que las albóndigas no se desarmen cuando estén en la salsa [ Música ] la pasta está servida lo que es este plato por favor increíble y sabe muy pero muy rico porque esto yo lo hice antes y me encantó por eso lo quiero compartir con ustedes pero igualmente en este canal siempre pero vamos a todos los platos así que vamos a ver qué tal [ Música ] no buenísima [ Música ] un montón de giro el pedo igual yo nunca como hace mucho siempre los cortos los vídeos bueno más o menos increíble realmente este plato tiene",
        "10 puntos",
        "11 puntos",
        "20 puntos muy muy ricos tienen que hacerlo quedan buenísimas no se ven arrepentir si les gustó el vídeo si les gustó en la receta los invito a que dejen un súper like que comparten el vídeo que dejen algún mensajito y por supuesto no olviden de suscribirse al canal apretando la fotito que aparece ahora acá abajo nos estaremos viendo hoy espero muy prontito chao chao [ Música ]"

"""

# Limpiar el texto de cualquier HTML (en caso de que haya)
soup = BeautifulSoup(text, "html.parser")
clean_text = soup.get_text()

# Eliminar caracteres no deseados usando expresiones regulares
clean_text = re.sub(r'\s+', ' ', clean_text)  # Reemplazar múltiples espacios por un solo espacio
clean_text = re.sub(r'\[.*?\]', '', clean_text)  # Eliminar contenido entre corchetes (e.g., [ Aplausos ])

# Tokenización de oraciones
sentences = sent_tokenize(clean_text)

# Imprimir oraciones tokenizadas
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")

