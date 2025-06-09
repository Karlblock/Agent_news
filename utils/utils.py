import json
from datetime import datetime

def save_training_example(prompt, response, topic):
    data = {
        "instruction": f"Fais une analyse sur : {topic}",
        "input": prompt,
        "output": response,
        "topic": topic,
        "timestamp": datetime.now().isoformat()
    }
    with open("training_data.jsonl", "a") as f:
        f.write(json.dumps(data) + "\n")
