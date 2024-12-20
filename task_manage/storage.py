import json
import os
from datetime import datetime

FILE_PATH = "task.json"

def load_task():
    """Load task from the JSON file"""

    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_task(tasks):
    """Save tasks to JSON file"""

    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)