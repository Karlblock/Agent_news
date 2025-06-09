from logger import setup_logger
logger = setup_logger(__name__)

import argparse
from agent.news_fetcher import get_rss_news
from agent.analyzer import analyze_with_model, extract_sources
from output.output_formatter import send_alert
from utils import save_training_example
from datetime import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, required=True, help="Sujet à analyser (ex: IA, PSG, politique)")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="Modèle IA à utiliser")
    parser.add_argument("--no-send", action="store_true", help="Ne pas envoyer sur Discord/Telegram")
    args = parser.parse_args()

    rss = get_rss_news(topic=args.topic)
    prompt, response = analyze_with_model(topic=args.topic, rss=rss, model=args.model)

    logger.info(f"Analyse terminée pour le sujet : {args.topic}")
    print(f"\n=== Analyse du sujet : {args.topic} ===\n{response}\n")

    # 🔧 Ajoute les sources en HTML si dispo
    sources_html = extract_sources(response)
    if sources_html.strip():
        full_text = f"{response}\n\n📎 Sources à consulter :\n{sources_html}"
    else:
        full_text = response

    save_training_example(prompt, response, topic=args.topic)

    if not args.no_send:
        send_alert(topic=args.topic, texte=full_text)
