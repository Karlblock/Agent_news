from logger import setup_logger
logger = setup_logger(__name__)

import os
from discord_output import send_to_discord
from telegram_output import send_to_telegram

def send_alert(topic, texte):
    try:
        message = f"📰 Sujet : **{topic}**\n\n{texte}"

        # Discord
        webhook = os.getenv("DISCORD_NEWS_WEBHOOK")
        if webhook:
            if len(message) > 1900:
                logger.warning("[Discord] Message trop long. Tronqué à 1900 caractères.")
                message = message[:1900] + "\n... (tronqué)"
            status, resp = send_to_discord(webhook, message)
            logger.info(f"[Discord] {status} – {resp}")

        # Telegram
        tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        tg_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if tg_token and tg_chat_id:
            status, resp = send_to_telegram(tg_token, tg_chat_id, message)
            if status == 404:
                logger.error("[Telegram] Chat ID non trouvé. Le bot est-il bien ajouté au canal ?")
            logger.info(f"[Telegram] {status} – {resp}")

    except Exception as e:
        logger.error(f"[ALERT] Erreur d'envoi : {e}")
