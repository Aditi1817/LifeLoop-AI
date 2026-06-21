"""
Helper utilities for LifeLoop AI
"""

import random
from datetime import datetime, timedelta

def get_sustainability_tip() -> str:
    """Get random sustainability tip"""
    tips = [
        "💡 Turn off lights when leaving a room",
        "🚶 Walk for trips under 1km",
        "♻️ Use reusable bags",
        "💧 Take shorter showers",
        "📱 Unplug phone charger",
        "🥤 Use a reusable water bottle",
        "🌿 Plant a tree",
        "📦 Recycle paper and plastic",
        "🚲 Bike instead of drive for short trips",
        "🥗 Eat more plant-based meals"
    ]
    return random.choice(tips)

def calculate_trees_needed(co2_kg: float) -> int:
    """Calculate trees needed to offset CO2"""
    return int(co2_kg / 21)

def get_motivational_message() -> str:
    """Get motivational message"""
    messages = [
        "Every small action creates ripples of change! 🌊",
        "You're making a difference! Keep going! 💪",
        "Together we can save the planet! 🌍",
        "Small steps lead to big impacts! 🚀",
        "Your actions matter! Thank you! 🙏"
    ]
    return random.choice(messages)

def format_date(date_str: str) -> str:
    """Format date string"""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%B %d, %Y")
    except:
        return date_str

def get_week_number() -> int:
    """Get current week number"""
    return datetime.now().isocalendar()[1]