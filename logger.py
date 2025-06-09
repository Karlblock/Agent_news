import logging
import os

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Console
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s – %(name)s – %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Fichier
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)
        file_handler = logging.FileHandler(os.path.join(log_dir, "agent_news.log"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
