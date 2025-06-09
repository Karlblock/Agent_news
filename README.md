# 🧠 Agent IA News

Agent IA News est un projet open source d’analyse automatisée de sujets d’actualité (comme “IA”, “PSG”, “politique”).
Il collecte les actualités via des flux RSS, analyse les contenus avec un modèle d’intelligence artificielle, puis publie automatiquement un résumé sur Discord et/ou Telegram.

## 🚀 Fonctionnalités

- 🔍 Lecture des flux RSS dynamiques + personnalisés (`feeds.txt`)
- 🤖 Analyse intelligente du sujet via API (1min.ai ou DeepSeek)
- 🔁 Fallback automatique si le sujet est filtré
- 🪵 Logs centralisés (`logs/agent_news.log`)
- 💬 Envoi automatique vers Discord et Telegram
- 🧩 Modularité du code pour extension future

## 📦 Installation

```bash
git clone https://github.com/Karlblock/Agent_News.git
cd Agent_News
make install
```

## ⚙️ Utilisation

```bash
Anews "intelligence artificielle"
```

Ou :

```bash
make run topic="PSG"
```

## 🔐 Configuration (.env)

```env
API_1MIN_KEY=your_1min_ai_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
DISCORD_NEWS_WEBHOOK=https://discord.com/api/webhooks/xxx
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## 🛠 Structure

- `main.py` – point d'entrée CLI
- `analyzer.py` – interaction avec les modèles d’IA
- `news_fetcher.py` – collecte RSS dynamique + personnalisée
- `feeds.txt` – flux personnalisés par sujet
- `output_formatter.py` – envoi vers Discord/Telegram
- `logger.py` – journalisation globale
- `logs/agent_news.log` – trace de toutes les exécutions

## 🧪 Exemple d'analyse

```bash
Anews "politique internationale"
```

## 📝 Licence

Ce projet est sous licence MIT – voir `LICENSE`.

## 👨‍💻 Auteur

Développé par [Karlblock](https://github.com/Karlblock) – Cyber Normandie.
