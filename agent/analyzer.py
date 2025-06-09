import os
import re
import requests
from openai import OpenAI
from dotenv import load_dotenv
from logger import setup_logger

logger = setup_logger(__name__)
load_dotenv()

API_1MIN_KEY = os.getenv("API_1MIN_KEY")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")



def extract_sources(response):
    urls = re.findall(r'(https?://[^\s]+)', response)
    unique_urls = list(set(urls))
    formatted = [f'• <a href="{url}">{url}</a>' for url in unique_urls]
    return "\n".join(formatted)



def analyze_with_model(topic, rss, model="gpt-4o-mini", prompt_template=None):
    if prompt_template:
        prompt = prompt_template.format(topic=topic, rss="\n".join(rss))
    else:
        prompt = (
        f"Tu es un analyste chargé d'analyser uniquement les actualités pertinentes liées au sujet suivant : \"{topic}\". "
        "Réponds en 1000 caractères max, avec un résumé synthétique. "
        "Ignore les contenus hors-sujet, géopolitiques ou violents. "
        "Structure ta réponse avec ces titres :\n"
        "📝 Résumé du sujet :\n"
        "📊 Tendances actuelles :\n"
        "⚠️ Risques ou opportunités :\n"
        "📰 News marquantes :\n"
        f"Voici les données brutes :\n{rss}"
    )

    if model == "deepseek-chat":
        client = OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com")
        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            stream=False
        )
        response_text = res.choices[0].message.content
        sources_html = extract_sources(response_text)
        return prompt, response_text

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
            response_text = result_object[0]
            sources_html = extract_sources(response_text)
            return prompt, response_text
        else:
            logger.warning(f"[IA] Aucune réponse générée pour le sujet : {topic}")
            return prompt, "Aucune réponse"
    elif res.status_code == 423:
        logger.warning(f"[IA] 423 – Contenu filtré, relance avec DeepSeek...")
        return analyze_with_model(topic, rss, model="deepseek-chat")
    elif res.status_code == 401:
        logger.error("❌ Clé API invalide. Vérifie API_1MIN_KEY dans .env.")
        return prompt, "[X] Clé API invalide. Vérifie .env"
    else:
        logger.error(f"[IA] Erreur {res.status_code} – {res.text}")
        return prompt, f"[X] Erreur {res.status_code} : {res.text}"

