import feedparser
from datetime import datetime, timedelta
import time
import re
import os
import requests

# Liste des sources RSS par thématique
RSS_SOURCES = {
    "Sport": [
        "https://www.espn.com/espn/rss/news",
        "https://www.espn.com/espn/rss/nba/news",
        "https://www.lequipe.fr/rss/actu_rss.xml",
    ],
    "IA": [
        "https://www.technologyreview.com/feed/",
        "https://venturebeat.com/feed/",
    ],
    "Crypto": [
        "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "https://cointelegraph.com/rss",
    ],
    "Politique": [
        "https://www.lemonde.fr/politique/rss_full.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
    ],
    "default": [
        "https://news.google.com/rss/search?q={topic}&hl=fr&gl=FR&ceid=FR:fr"
    ]
}

def is_valid_rss(url):
    try:
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return False
        parsed = feedparser.parse(res.content)
        return bool(parsed.entries)
    except:
        return False

def get_rss_news(topic, debug=False):
    now = datetime.utcnow()
    cutoff = now - timedelta(hours=24)

    base_topic = topic.split("–")[0].strip()
    rss_urls = RSS_SOURCES.get(base_topic, RSS_SOURCES["default"])
    rss_urls = [url.format(topic=topic) for url in rss_urls]

    # Ajout des sources dynamiques depuis fichier texte
    custom_sources_path = f"sources/{base_topic}.txt"
    if os.path.exists(custom_sources_path):
        with open(custom_sources_path, "r") as f:
            for line in f:
                url = line.strip()
                if url.startswith("http") and is_valid_rss(url):
                    rss_urls.append(url)
                elif debug:
                    print(f"[DEBUG] Source ignorée (invalide) : {url}")

    news = []
    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                published = entry.get("published_parsed")
                if not published:
                    continue

                published_dt = datetime.fromtimestamp(time.mktime(published))
                if published_dt < cutoff:
                    continue  # trop ancien

                if re.search(r"\\b(202[0-3])\\b", entry.title):
                    continue

                date_str = published_dt.strftime("%Y-%m-%d %H:%M")
                formatted = f"- [{date_str}] {entry.title.strip()} ({entry.link.strip()})"
                news.append(formatted)

                if debug:
                    print(f"[DEBUG] Gardé : {formatted}")

        except Exception as e:
            error_msg = f"⚠️ Erreur avec le flux : {url} ({e})"
            news.append(error_msg)
            if debug:
                print(error_msg)

    news.sort(reverse=True)
    return news[:10]  # Limite à 10 résultats récents maximum

def append_new_sources(topic, sources_html):
    base_topic = topic.split("–")[0].strip()
    filepath = f"sources/{base_topic}.txt"

    urls = re.findall(r'https?://[^\s"<>]+', sources_html)
    os.makedirs("sources", exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass

    with open(filepath, "r") as f:
        known_urls = set(line.strip() for line in f if line.strip())

    new_urls = [url for url in urls if url not in known_urls and is_valid_rss(url)]
    if new_urls:
        with open(filepath, "a") as f:
            for url in new_urls:
                f.write(url + "\n")
        print(f"🆕 {len(new_urls)} nouvelles sources ajoutées dans {filepath}")
    else:
        print(f"✅ Aucune nouvelle source à ajouter pour {base_topic}")
