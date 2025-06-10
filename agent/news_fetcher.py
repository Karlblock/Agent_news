import feedparser
from datetime import datetime, timedelta
import time
import re
from urllib.parse import quote_plus

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

def get_rss_news(topic, debug=False):
    now = datetime.utcnow()
    cutoff = now - timedelta(hours=24)

    base_topic = topic.split("–")[0].strip()
    rss_urls = RSS_SOURCES.get(base_topic, RSS_SOURCES["default"])

    encoded_topic = quote_plus(topic)
    rss_urls = [url.format(topic=encoded_topic) for url in rss_urls]

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

                # ❌ Skip les titres qui mentionnent une année trop ancienne dans le titre (ex: "2021")
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

    # Trie les news récentes par date descendante
    news.sort(reverse=True)
    return news[:10]  # Limite à 10 résultats récents maximum
