#!/bin/bash
echo "🔧 Installation de l'agent IA News..."

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

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

echo "🛠 Création du binaire global Anews..."

cat <<EOF | sudo tee /usr/local/bin/Anews > /dev/null
#!/bin/bash
PROJECT_DIR="\$HOME/Agent_news"  # <- adapte ce chemin si nécessaire
VENV_DIR="\$PROJECT_DIR/venv"

if [ ! -d "\$VENV_DIR" ]; then
  echo "❌ Environnement virtuel non trouvé dans \$VENV_DIR. Lancez ./install.sh d'abord."
  exit 1
fi

source "\$VENV_DIR/bin/activate"

cd "\$PROJECT_DIR"
python3 main.py "\$@"
EOF

sudo chmod +x /usr/local/bin/Anews
echo "✅ Binaire Anews installé dans /usr/local/bin"
echo "✅ Installation terminée."
