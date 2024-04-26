from flask import Flask
import random
import requests

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50 por ciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>En la siguiente página podrás aprender sobre las dependencias tecnológicas!</h1><a href="/random">Ver un dato</a><br><a href="/ima">Ver una imagen</a>'

@app.route('/random')
def otro():
    return f'<p>{random.choice(facts_list)}</p><a href="/">Regresar a inicio</a>'

@app.route("/ima")
def get_duck_image():
    url = "https://random-d.uk/api/random"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        return f'<img src="{data["url"]}" alt="Random Duck"/><a href="/">Regresar a inicio</a>'
    except requests.RequestException:
        return 'No se pudo cargar la imagen. <a href="/">Regresar a inicio</a>'

app.run(debug=True)
