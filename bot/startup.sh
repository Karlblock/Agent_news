#!/bin/bash

# Activation de l'environnement virtuel
source venv/bin/activate

# Vérification de l'argument
if [ -z "$1" ]; then
  echo "❌ Sujet manquant. Utilisation : ./startup.sh \"sujet_exemple\""
  exit 1
fi

# Lancement de l’agent avec le sujet donné
python main.py --topic "$1"
