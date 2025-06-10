import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from logger import setup_logger

logger = setup_logger(__name__)
load_dotenv()

DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")

def extract_sources(response):
    urls = re.findall(r'(https?://[^\s]+)', response)
    unique_urls = list(set(urls))
    formatted = [f'• <a href="{url}">{url}</a>' for url in unique_urls]
    return "\n".join(formatted)


def analyze_with_model(topic, rss, model="deepseek-chat"):
    prompt = (
        f"Tu es un analyste chargé d’analyser les actualités des dernières 24h sur : « {topic} ».\n"
        f"{rss}\n"
        "Structure ta réponse avec :\n"
        "📈 Mouvement ou annonce clé :\n"
        "🔐 Incident ou alerte :\n"
        "🏛️ Cadre réglementaire :\n"
        "📰 Source confirmée :"
    )

    if model == "deepseek-chat":
        client = OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com")
        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        return prompt, res.choices[0].message.content

    elif model == "mistral-large-latest":
        from mistralai import Mistral
        mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
        res = mistral_client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        return prompt, res.choices[0].message.content

    else:
        raise ValueError(f"Modèle non supporté : {model}")
