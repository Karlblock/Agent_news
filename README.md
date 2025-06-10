# 🧠 Agent IA News – v0.4.0

Agent IA News est un agent open source de veille automatisée. Il collecte les dernières actualités via RSS, les analyse avec un modèle d’intelligence artificielle (DeepSeek ou Mistral), puis envoie un résumé formaté vers Discord et/ou Telegram.

## 🚀 Fonctionnalités principales

- 🔎 **Flux RSS par thème** (IA, sport, crypto, politique…) + support de flux personnalisés
- 🤖 **Analyse IA** par `deepseek-chat` ou `mistral-large-latest`
- 🪝 **Publication automatisée** vers Discord & Telegram
- 🧠 **Interface CLI interactive** (choix du modèle, thème, sous-sujet)
- 🕵️‍♂️ **Filtrage automatique** des actualités < 24h
- 🧩 **Architecture modulaire** : prompts, analyse, envoi, logs, etc.
- 📁 **Sauvegarde automatique** des prompts/réponses dans `data/training_examples/`

---

## ⚙️ Installation

```bash
git clone https://github.com/Karlblock/Agent_News.git
cd Agent_News
make install
```

---

## 🔐 Configuration `.env`

```env
DEEPSEEK_API_KEY=your_deepseek_api_key
MISTRAL_API_KEY=your_mistral_api_key

DISCORD_NEWS_WEBHOOK=https://discord.com/api/webhooks/xxx
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## 🧪 Utilisation (2 façons)

### ➤ CLI interactive

```bash
Anews
```

- Choisis un modèle IA (`deepseek-chat` ou `mistral-large-latest`)
- Sélectionne une thématique (IA, sport, crypto, etc.)
- Ajoute un sous-sujet facultatif (ex : "NBA", "ETH", "Élections européennes")

### ➤ Exécution directe (mode script)

```bash
make run topic="Crypto – BTC" model="mistral-large-latest"
```

---

## 📦 Structure du projet

```
Agent_News/
├── main.py                 # Point d’entrée CLI
├── install.sh              # Script d'installation global
├── Makefile                # Raccourcis d'exécution
├── prompts/                # Prompts IA par thématique
├── agent/
│   ├── analyzer.py         # Appels aux modèles IA (DeepSeek, Mistral)
│   ├── news_fetcher.py     # Collecte et filtrage RSS (< 24h)
│   └── feeds.txt           # Flux RSS personnalisés
├── output/
│   └── output_formatter.py # Envoi vers Discord / Telegram
├── utils/
│   ├── save_training.py    # Sauvegarde des exemples d'entraînement
│   └── ...
├── logger.py               # Logger central
├── logs/agent_news.log     # Log complet d'activité
└── .env                    # Clés d'API
```

---

## 💬 Exemple d'analyse

```bash
Anews
```

```
🧠 Modèle sélectionné : deepseek-chat
📚 Sujet : Crypto – BTC
🔍 Résumé généré automatiquement :
  - 📈 Mouvement ou annonce clé : ...
  - 🔐 Incident ou alerte : ...
  - 🏛️ Cadre réglementaire : ...
  - 📰 Source confirmée : ...
```

---

## 📜 Licence

Code distribué sous licence **MIT**.

---

## 👨‍💻 Auteur

Développé par [Karlblock](https://github.com/Karlblock)  
