from flask import Flask, jsonify
from raspagem import busca_pessoa


app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False

@app.route("/")
def inicio():
    dados = busca_pessoa()
    return jsonify(dados)


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'

if __name__ == "__main__":
    app.run(debug=True)
