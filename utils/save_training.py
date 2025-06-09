import os
from datetime import datetime

def save_training_example(prompt, response, topic="unknown", folder="training_examples"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder}/{topic}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== Prompt ===\n")
        f.write(prompt + "\n\n")
        f.write("=== Response ===\n")
        f.write(response)
