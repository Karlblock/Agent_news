from logger import setup_logger
logger = setup_logger(__name__)

import requests

def format_tldr(info):
    message = f"🧠 **Analyse IA – {info.get('url_blog', '')}**\n\n"
    message += f"**Prix actuel :** {info.get('prix', 'N/A')}\n"
    message += f"**Tendance générale :** {info.get('tendance', 'N/A')}\n\n"

    if info.get("risques"):
        message += "**⚠️ Risques :**\n" + "\n".join(f"- {r}" for r in info["risques"]) + "\n\n"
    if info.get("opportunites"):
        message += "**💡 Opportunités :**\n" + "\n".join(f"- {o}" for o in info["opportunites"]) + "\n\n"
    if info.get("news"):
        message += "**🗞 News :**\n" + "\n".join(f"- {n}" for n in info["news"]) + "\n"

    return message

def send_to_discord(webhook_url, message):
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    try:
        resp = requests.post(webhook_url, json=data, headers=headers)
        logger.info(f"[Discord] {resp.status_code} – {resp.text}")
        return resp.status_code, resp.text
    except Exception as e:
        logger.error(f"[Discord] Erreur : {e}")
        return 500, str(e)
