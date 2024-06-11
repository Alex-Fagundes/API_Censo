from flask import Flask
import json
import dados_import


app = Flask(__name__)

tabela_dados = dados_import.dados_2023


@app.route("/")
def listar_regiao():
    regioes = {"regiões": {}}
    tabela = tabela_dados[["regiao", "sigla_uf", "uf"]]
    tabela = tabela.drop_duplicates(ignore_index=True)
    for regiao, dados in tabela.groupby("regiao"):
        regioes["regiões"][regiao] = {
            linha["sigla_uf"]: linha["uf"] for i, linha in dados.iterrows()
        }
    # regioes = json.dumps(regioes)
    return regioes


app.run()
