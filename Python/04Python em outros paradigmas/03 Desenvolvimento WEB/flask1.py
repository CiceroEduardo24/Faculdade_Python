from flask import Flask

app = Flask(__name__) #argumento para que o Flask consiga localizar,
                      #na aplicação, arquivos estáticos, como css e javascript,
                      #e arquivos de modelos (templates), se for o caso.
@app.route('/')       # utilizamos o decorador @app.route(‘/’) para criar uma rota
                      # para a URL raiz da nossa aplicação (‘/’). Esse decorador espera
                      # como parâmetro a rota, ou URL, que será utilizada no navegador, por exemplo.
def ola_mundo():
    return "Olá, mundo."


if __name__ == '__main__':
    app.run()