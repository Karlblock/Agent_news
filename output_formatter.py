from logger import setup_logger
logger = setup_logger(__name__)

import os
from discord_output import format_tldr, send_to_discord
from telegram_output import send_to_telegram

def send_alert(topic, texte):
    try:
        message = f"📰 Sujet : **{topic}**\n\n{texte}"

        webhook = os.getenv("DISCORD_NEWS_WEBHOOK")
        if webhook:
            status, resp = send_to_discord(webhook, message)
            logger.info(f"[Discord] {status} – {resp}")

        tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        tg_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if tg_token and tg_chat_id:
            status, resp = send_to_telegram(tg_token, tg_chat_id, message)
            logger.info(f"[Telegram] {status} – {resp}")
    except Exception as e:
        logger.error(f"[ALERT] Erreur envoi : {e}")
