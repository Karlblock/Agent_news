from prompt_toolkit import prompt
from rich.console import Console
from rich.table import Table
import argparse
from logger import setup_logger
from agent.analyzer import analyze_with_model, extract_sources
from agent.news_fetcher import get_rss_news
from output.output_formatter import send_alert
from prompts.prompts_dict import PROMPT_BY_TOPIC
from utils import save_training_example

console = Console()
logger = setup_logger(__name__)

AVAILABLE_MODELS = ["deepseek-chat", "mistral-large-latest"]

def choisir_modele():
    console.print("\n[bold yellow]🧠 Choisis un modèle IA[/bold yellow]")
    for i, model in enumerate(AVAILABLE_MODELS):
        console.print(f"[bold green][{i}][/bold green] {model}")
    choix = prompt("👉 Entrez le numéro du modèle [0 par défaut] : ").strip()
    try:
        index = int(choix) if choix else 0
        return AVAILABLE_MODELS[index]
    except Exception:
        console.print("❌ [bold red]Entrée invalide. Fermeture.[/bold red]")
        exit(1)

def choisir_categorie():
    console.print("\n[bold cyan]🧠 Choisis une catégorie d'analyse[/bold cyan]")
    keys = list(PROMPT_BY_TOPIC.keys())

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Numéro", justify="center")
    table.add_column("Catégorie")

    for i, key in enumerate(keys):
        table.add_row(str(i), key)

    console.print(table)

    try:
        index_str = prompt("🎯 Entrez le numéro de la catégorie [0 par défaut] : ").strip()
        index = int(index_str) if index_str else 0

        if 0 <= index < len(keys):
            console.print(f"\n✅ Catégorie sélectionnée : [bold green]{keys[index]}[/bold green]")
            return keys[index]
        else:
            raise ValueError
    except (ValueError, KeyboardInterrupt):
        console.print("❌ [bold red]Entrée invalide. Fermeture.[/bold red]")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, help="Modèle IA à utiliser (ex: deepseek-chat)")
    parser.add_argument("--no-send", action="store_true", help="Ne pas envoyer sur Discord/Telegram")
    args = parser.parse_args()

    model = args.model or choisir_modele()
    topic = choisir_categorie()
    sous_sujet = prompt("📝 (Optionnel) Sujet plus précis ? ").strip()
    full_topic = f"{topic} – {sous_sujet}" if sous_sujet else topic

    rss = get_rss_news(topic=full_topic)
    prompt_template = PROMPT_BY_TOPIC.get(topic, PROMPT_BY_TOPIC.get("default"))

    prompt_text, response = analyze_with_model(
        topic=full_topic,
        rss=rss,
        model=model,
    )

    sources = extract_sources(response)
    response_with_sources = response + ("\n\n📎 <b>Sources à consulter :</b>\n" + sources if sources else "")

    logger.info(f"Analyse terminée pour : {full_topic}")
    print(f"\n=== 🧠 Analyse du sujet : {full_topic} ===\n{response_with_sources}\n")

    save_training_example(prompt_text, response_with_sources, topic=full_topic)

    if not args.no_send:
        send_alert(topic=full_topic, texte=response_with_sources)
