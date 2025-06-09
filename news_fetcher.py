import feedparser

def get_rss_news(topic, max_entries=5):
    sources = [
        f"https://news.google.com/rss/search?q={topic}",
        f"https://www.bing.com/news/search?q={topic}&format=rss"
    ]

    news = []
    for url in sources:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_entries]:
            title = entry.get("title", "Sans titre")
            link = entry.get("link", "#")
            summary = entry.get("summary", "").split('.')[0]
            news.append(f"{title} - {summary}")
    return "\n".join(news)
