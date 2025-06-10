import os
from datetime import datetime

def save_training_example(prompt, output, topic="default"):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    directory = "data/training_examples"

    # Protection contre les conflits fichier vs. dossier
    if os.path.isfile(directory):
        raise RuntimeError(f"❌ Un fichier existe déjà à l'emplacement : {directory}. Supprime-le pour continuer.")

    os.makedirs(directory, exist_ok=True)

    filename = os.path.join(directory, f"{today}__{topic.replace(' ', '_')}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("PROMPT:\n" + prompt + "\n\nRESPONSE:\n" + output)
