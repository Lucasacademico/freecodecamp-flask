
# Definido funcionalidade 'render_template'
from flask import Flask, render_template
app = Flask(__name__)

# Método 'render_template' foi chamado e carrega o arquivo 'home.html' da pasta 'templates'
# Podemos gerar mais de uma rota
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
