from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Gabriel, o Palmeiras não tem mundial"

if __name__ == '__main__':
    app.run()