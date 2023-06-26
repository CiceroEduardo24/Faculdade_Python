from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Página principal"

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome):
    return "Olá, " + nome
#criamos a rota para a função logar e passamos como argumento uma lista contendo duas strings,
#‘GET’ e ‘POST’ (linha 15). Isso indica que essa rota deve responder às requisições do tipo GET e POST.
@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."

if __name__ == '__main__':
    app.run()