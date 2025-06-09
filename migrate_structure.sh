#!/bin/bash
echo "📦 Réorganisation du projet Agent_News..."

mkdir -p agent bot output config logs

# Moteur IA
mv analyzer.py news_fetcher.py utils.py training_data.jsonl agent/ 2>/dev/null

# Telegram
mv telegram_bot.py telegram_output.py startup.sh bot/ 2>/dev/null

# Output formatters
mv discord_output.py output_formatter.py output/ 2>/dev/null

# split util
mv split_message.py output/ 2>/dev/null

# Config
mv feeds.txt config/ 2>/dev/null
mv .env config/ 2>/dev/null

echo "✅ Structure mise à jour."
echo "Pense à adapter les chemins d'import dans tes fichiers (e.g. from agent.analyzer import ...)"
