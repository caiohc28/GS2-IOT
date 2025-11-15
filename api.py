from flask import Flask, jsonify
from gerar_missoes import gerar_missoes_semanais
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# ---------------------------------------------------------
# Função para carregar missões do arquivo JSON
# ---------------------------------------------------------
def carregar_missoes():
    if not os.path.exists("missoes_semanais.json"):
        print("Arquivo não encontrado. Gerando missões novas...")
        return gerar_missoes_semanais()

    with open("missoes_semanais.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Verificar se já passou 1 semana
    data_arquivo = datetime.strptime(data["data"], "%d/%m/%Y")
    if datetime.now() - data_arquivo > timedelta(days=7):
        print("Missões desatualizadas. Gerando novas...")
        return gerar_missoes_semanais()

    return data


# ---------------------------------------------------------
# ENDPOINT 1 → Retorna as missões semanais
# ---------------------------------------------------------
@app.get("/missoes")
def get_missoes():
    missoes = carregar_missoes()
    return jsonify(missoes)


# ---------------------------------------------------------
# ENDPOINT 2 → Força gerar novas missões (útil para testes)
# ---------------------------------------------------------
@app.post("/missoes/gerar")
def gerar_novas():
    resultado = gerar_missoes_semanais()
    return jsonify(resultado)


# ---------------------------------------------------------
# Iniciar servidor
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
