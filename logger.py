import logging
import os
from datetime import datetime

def setup_logger(name: str):
    # Crée le dossier logs si besoin
    os.makedirs("logs", exist_ok=True)

    # Nom de fichier basé sur la date
    log_filename = datetime.now().strftime("logs/%Y-%m-%d.log")

    # Création du logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Évite les handlers dupliqués
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter("[%(levelname)s] %(message)s")
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        # Fichier handler
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger
