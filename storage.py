import json
from pathlib import Path

DATA_FILE = Path("data.json")

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tours": [], "customers": [], "bookings": []}