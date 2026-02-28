import json
import os

DATA_FILE = "school_data.json"


class OutOfLimitError(Exception):
    """Custom exception for menu range errors."""
    pass


def load_data():
    """Load data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)