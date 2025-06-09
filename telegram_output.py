from logger import setup_logger
logger = setup_logger(__name__)

import requests

def send_to_telegram(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=data)
        logger.info(f"[Telegram] Statut {response.status_code} – {response.text}")
        return response.status_code, response.text
    except Exception as e:
        logger.error(f"[Telegram] Erreur : {e}")
        return 500, str(e)
