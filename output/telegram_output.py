import requests
from logger import setup_logger
from utils.formatting import markdown_to_html

logger = setup_logger(__name__)

def send_to_telegram(token, chat_id, text):
    if not token or not chat_id:
        logger.warning("[Telegram] Token ou Chat ID manquant.")
        return 400, "Token ou Chat ID manquant."

    html_text = markdown_to_html(text)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": html_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    try:
        response = requests.post(url, json=payload)
        return response.status_code, response.text
    except Exception as e:
        logger.error(f"[Telegram] Erreur d'envoi : {e}")
        return 500, str(e)
