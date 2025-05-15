from datetime import datetime, timedelta
from dateutil import parser as date_parser
import re

def process_task(task_text):
    task_text_lower = task_text.lower()

    # Priority
    priority = "Medium"
    if "urgent" in task_text_lower or "important" in task_text_lower:
        priority = "High"
    elif "low" in task_text_lower:
        priority = "Low"

    # Category detection
    categories = ["work", "personal", "study", "health", "shopping"]
    category = next((cat.capitalize() for cat in categories if cat in task_text_lower), "General")

    # Due date parsing
    due_date = extract_due_date(task_text_lower)

    return {
        "task": task_text,
        "priority": priority,
        "category": category,
        "due": due_date
    }

def extract_due_date(text):
    today = datetime.now().date()
    keywords = {
        "today": today,
        "day after tomorrow": today + timedelta(days=2),
        "tomorrow": today + timedelta(days=1),
        "next week": today + timedelta(weeks=1),
        "yesterday": today - timedelta(days=1),
        "day before yesterday": today - timedelta(days=2)
    }

    for k, v in keywords.items():
        if k in text:
            return v.isoformat()

    # Try parsing with dateutil
    try:
        parsed_date = date_parser.parse(text, fuzzy=True).date()
        return parsed_date.isoformat()
    except:
        return today.isoformat()
