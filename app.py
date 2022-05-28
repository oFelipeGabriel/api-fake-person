from flask import Flask, jsonify
from raspagem import busca_pessoa

app = Flask(__name__)

@app.route("/")
def hello_world():
    dados = busca_pessoa()
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)