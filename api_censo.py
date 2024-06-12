from flask import Flask, jsonify
import dados_import


app = Flask(__name__)

dataframe = dados_import.dados_2023


@app.route("/escola")
def exibir_dados():
    dados = dataframe.head(50).to_dict(orient="records")
    return jsonify({"escolas": dados})


app.run()
