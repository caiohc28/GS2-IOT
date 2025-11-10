import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurar a API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gerar_missao(area):
    prompt = f"""
    Gere uma missão curta, prática e inspiradora na área de {area}, com foco em sustentabilidade e resolução de problemas reais.
    A resposta deve estar no formato JSON, contendo exatamente:
    - "titulo": nome curto e criativo da missão;
    - "objetivo": uma frase clara explicando o que o participante deve fazer (ex: "Crie um protótipo que ajude a reduzir o desperdício de água na sua comunidade");
    - "moral": uma frase curta com o aprendizado ou impacto positivo da missão.

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

        # 🔧 Remover blocos de markdown como ```json ... ```
        texto_limpo = re.sub(r"```json|```", "", texto).strip()

        # Converter para JSON válido
        missao = json.loads(texto_limpo)
        return json.dumps(missao, indent=2, ensure_ascii=False)

    except json.JSONDecodeError:
        return f"Resposta não está em formato JSON válido:\n\n{texto}"
    except Exception as e:
        return f"Erro ao gerar missão: {e}"

if __name__ == "__main__":
    area = input("Área de interesse: ")
    print("\nMissão gerada pela IA (JSON):\n")
    print(gerar_missao(area))
