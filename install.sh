#!/bin/bash

echo "🔧 Installation de l'agent IA News..."

# Création de l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Mise à jour pip
pip install --upgrade pip

# Installation des dépendances
pip install -r requirements.txt

# Création du fichier .env si absent
if [ ! -f ".env" ]; then
  echo "🔐 Création du fichier .env..."
  cat <<EOF > .env
API_1MIN_KEY=your_1min_ai_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
DISCORD_NEWS_WEBHOOK=https://discord.com/api/webhooks/xxx
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
EOF
  echo "✅ Fichier .env créé. Pense à le remplir."
else
  echo "ℹ️ Le fichier .env existe déjà. Vérifie son contenu."
fi

echo "✅ Installation terminée."
