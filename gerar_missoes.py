import google.generativeai as genai
import os
import json
import re
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Lista das áreas do aplicativo
AREAS_INTERESSE = [
    "Inteligência Artificial",
    "Sustentabilidade",
    "Programação",
    "Design",
    "Empreendedorismo",
    "Educação",
    "Saúde e Bem-estar",
    "Inclusão e Diversidade"
]

def gerar_missao(area):
    """Gera uma missão curta e inspiradora para uma área de interesse."""
    prompt = f"""
    Gere uma missão curta, prática e inspiradora na área de {area}, com foco em sustentabilidade, inovação e resolução de problemas reais.
    A resposta deve estar em formato JSON com os seguintes campos:
    - "titulo": nome curto e criativo da missão
    - "objetivo": uma frase clara explicando o que o usuário deve fazer
    - "moral": uma frase curta com o aprendizado ou impacto positivo

    Exemplo:
    {{
      "titulo": "Energia do Futuro",
      "objetivo": "Crie um protótipo que use energia limpa para resolver um problema cotidiano.",
      "moral": "Pequenas ideias sustentáveis podem gerar grandes transformações."
    }}
    """

    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        resposta = model.generate_content(prompt)
        texto = resposta.text.strip()
        texto_limpo = re.sub(r"```json|```", "", texto).strip()
        missao = json.loads(texto_limpo)
        return missao
    except Exception as e:
        return {"erro": f"Falha ao gerar missão para {area}: {e}"}


def gerar_missoes_semanais():
    """Gera uma missão por semana para cada área de interesse."""
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    print(f"📅 Gerando missões semanais ({data_hoje})...\n")

    missoes = {}

    for area in AREAS_INTERESSE:
        print(f"🔹 Gerando missão para {area}...")
        missao = gerar_missao(area)
        missoes[area] = missao

    # Salvar resultado em JSON para integração futura com o app
    with open("missoes_semanais.json", "w", encoding="utf-8") as f:
        json.dump({
            "data": data_hoje,
            "missoes": missoes
        }, f, indent=2, ensure_ascii=False)

    print("\n✅ Missões geradas e salvas em 'missoes_semanais.json'")
    return missoes


if __name__ == "__main__":
    gerar_missoes_semanais()
