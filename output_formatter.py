import os
from discord_output import format_tldr, send_to_discord
from telegram_output import send_to_telegram  # à créer

def send_alert(topic, texte):
    try:
        message = f"📰 Sujet : **{topic}**\n\n{texte}"
        # Discord
        webhook = os.getenv("DISCORD_NEWS_WEBHOOK")
        if webhook:
            status, resp = send_to_discord(webhook, message)
            print(f"[✓] Discord envoyé (code {status})")

        # Telegram
        tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        tg_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if tg_token and tg_chat_id:
            send_to_telegram(tg_token, tg_chat_id, message)

    except Exception as e:
        print(f"[X] Erreur d'envoi : {e}")

