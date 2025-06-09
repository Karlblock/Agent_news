import feedparser
import os
from logger import setup_logger

logger = setup_logger(__name__)

def get_rss_news(topic, max_entries=5, feed_file="feeds.txt"):
    dynamic_feeds = [
        f"https://news.google.com/rss/search?q={topic}",
        f"https://www.bing.com/news/search?q={topic}&format=rss"
    ]

    custom_feeds = []
    if os.path.exists(feed_file):
        with open(feed_file, "r") as f:
            custom_feeds = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    feeds = list(set(dynamic_feeds + custom_feeds))
    news = []

    for url in feeds:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:max_entries]:
                title = entry.get("title", "Sans titre")
                summary = entry.get("summary", "").split('.')[0]
                news.append(f"{title} - {summary}")
        except Exception as e:
            logger.error(f"[RSS] Erreur de parsing sur {url} : {e}")

    if not news:
        logger.warning("Aucune actualité trouvée dans les flux RSS.")
    return "\n".join(news)
