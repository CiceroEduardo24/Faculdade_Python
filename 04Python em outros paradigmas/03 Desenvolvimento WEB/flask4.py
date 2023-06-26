from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Página principal."

@app.route('/ola/<nome>') #O decorador de rota (route) também permite que sejam passados parâmetros para as funções.
                          #Para isso, devemos colocar o nome do parâmetro da função entre < e> na URL da rota.
def ola_mundo(nome):
    return "Olá, " + nome

if __name__ == '__main__':
    app.run()