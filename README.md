# 🧠 Agent IA News – Analyse automatique de l’actualité par sujet

Ce projet permet d’analyser n’importe quel sujet (ex: IA, Sport, politique) à l’aide d’un modèle d’IA et d’un flux d’actualités.

## 🚀 Fonctionnalités

- 🔍 Récupère automatiquement des actualités RSS sur un sujet donné
- 🧠 Analyse et synthèse via API IA (1min.ai ou DeepSeek)
- 📤 Envoie automatique sur Discord ou Telegram
- 🗃 Enregistre les prompts et réponses pour fine-tuning

## 📦 Installation

```bash
git clone https://github.com/tonrepo/agent_news.git
cd agent_news
./install.sh
```

## ⚙️ Utilisation

```bash
./startup.sh "intelligence artificielle"
```

Ou manuellement :

```bash
source venv/bin/activate
python main.py --topic "psg"
```

## 🧪 Variables d'environnement

Configure le fichier `.env` :

```
API_1MIN_KEY=your_1min_ai_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
DISCORD_NEWS_WEBHOOK=https://discord.com/api/webhooks/xxx
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

## 🛣️ Roadmap

- [ ] Support complet de Telegram
- [ ] Interface Web minimaliste


---

© 2025 – Cyber Normandie
