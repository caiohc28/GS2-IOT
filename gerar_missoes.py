import google.generativeai as genai
import os
import json
import re
import oracledb
from datetime import datetime
from dotenv import load_dotenv

# ---------------------------------------------------------
# 1. Carregar variável da IA do .env
# ---------------------------------------------------------
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Configurar API Gemini
genai.configure(api_key=GEMINI_KEY)

# ---------------------------------------------------------
# 2. Credenciais Oracle FIXAS no código
# ---------------------------------------------------------
ORACLE_USER = "RM554518"
ORACLE_PASSWORD = "290805"
ORACLE_DSN = "oracle.fiap.com.br:1521/ORCL"


# ---------------------------------------------------------
# 3. Buscar áreas existentes no Oracle
# ---------------------------------------------------------
def buscar_areas_no_banco():
    try:
        conn = oracledb.connect(
            user=ORACLE_USER,
            password=ORACLE_PASSWORD,
            dsn=ORACLE_DSN
        )

        cursor = conn.cursor()
        cursor.execute("SELECT NOME FROM AREAS ORDER BY NOME")

        areas = [row[0] for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return areas

    except Exception as e:
        print(f"❌ Erro ao buscar áreas no banco: {e}")
        return []


# ---------------------------------------------------------
# 4. Gerar missão individual
# ---------------------------------------------------------
def gerar_missao(area):
    prompt = f"""
    Gere uma missão curta, prática e inspiradora na área de {area}, com foco em 
    sustentabilidade, inovação e resolução de problemas reais.

    A resposta deve estar em JSON, contendo:
    - "titulo": nome curto da missão
    - "objetivo": o que o usuário deve fazer
    - "moral": impacto positivo ou lição final
    """

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        resposta = model.generate_content(prompt)

        texto = resposta.text.strip()
        texto = re.sub(r"```json|```", "", texto).strip()

        missao = json.loads(texto)
        return missao

    except Exception as e:
        return {"erro": f"Erro ao gerar missão para {area}: {e}"}


# ---------------------------------------------------------
# 5. Gerar missões semanais baseadas nas áreas do Banco
# ---------------------------------------------------------
def gerar_missoes_semanais():
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    print(f"\n📅 Gerando missões semanais ({data_hoje})...\n")

    areas = buscar_areas_no_banco()

    if not areas:
        print("⚠ Nenhuma área encontrada no banco.")
        return

    missoes = {}

    for area in areas:
        print(f"🔹 Gerando missão para {area}...")
        missoes[area] = gerar_missao(area)

    resultado = {
        "data": data_hoje,
        "missoes": missoes
    }

    with open("missoes_semanais.json", "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    print("\n✅ Missões geradas e salvas em 'missoes_semanais.json'")
    return resultado


# ---------------------------------------------------------
# 6. Rodar o script
# ---------------------------------------------------------
if __name__ == "__main__":
    gerar_missoes_semanais()
