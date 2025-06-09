import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from logger import setup_logger

logger = setup_logger(__name__)
load_dotenv()

API_1MIN_KEY = os.getenv("API_1MIN_KEY")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")

def analyze_with_model(topic, rss, model="gpt-4o-mini"):
    prompt = (
        f"Tu es un expert du domaine '{topic}'. Donne une synthèse neutre et structurée :\n"
        "Résumé du sujet :\n"
        "Tendances actuelles :\n"
        "Risques ou opportunités à noter :\n"
        "Actualités marquantes :\n"
        f"Voici les infos disponibles :\n{rss}\n"
        "Analyse uniquement à partir de ces éléments. Ne fais pas de recommandations."
    )

    if model == "deepseek-chat":
        client = OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com")
        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            stream=False
        )
        return prompt, res.choices[0].message.content

    headers = {"API-KEY": API_1MIN_KEY, "Content-Type": "application/json"}
    data = {
        "type": "CHAT_WITH_AI",
        "model": model,
        "promptObject": {"prompt": prompt}
    }

    res = requests.post("https://api.1min.ai/api/features", headers=headers, json=data)
    if res.status_code == 200:
        result = res.json()
        result_object = result.get("aiRecord", {}).get("aiRecordDetail", {}).get("resultObject", [])
        if result_object:
            return prompt, result_object[0]
        else:
            logger.warning(f"[IA] Aucune réponse générée pour le sujet : {topic}")
            return prompt, "Aucune réponse"
    else:
        logger.error(f"[IA] Erreur {res.status_code} – {res.text}")
        return prompt, f"[X] Erreur {res.status_code} : {res.text}"
