from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# Nova rota exemplo 1
# # Criado nova rota para página 'market'
# # Pagina market.html criado em templates
# # Criado variavel 'item_name' para chamar direto no 'market.html'
# @app.route('/market')
# def market_page():
#     return render_template('market.html', item_name='Phone')

# Rota exemplo 2
# Utilizando dicionario para multiplos dados

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
