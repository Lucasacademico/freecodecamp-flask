# Aplicação base de uso flask
from flask import Flask
app = Flask(__name__)


# Acesso: http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "<h1>Hello, World</h1>"

# Acesso: http://127.0.0.1:5000/about
@app.route('/about')
def about_page():
    return '<h1>About Page</h1>'

# Acesso: http://127.0.0.1:5000/Lucas
@app.route('/about/<username>')
def username_about_page(username):
    return f'<h1>This is the about page of {username}</h1>'



if __name__ == '__main__':
    app.run(debug=True)


