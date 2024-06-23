from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route('/')
def hello_world():
    return 'Olá, mundo!'

# Roda a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
