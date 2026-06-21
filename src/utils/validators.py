"""
Input validators for LifeLoop AI
"""

import re

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> bool:
    """Validate password strength"""
    return len(password) >= 8

def validate_name(name: str) -> bool:
    """Validate name"""
    return len(name.strip()) >= 2

def sanitize_text(text: str) -> str:
    """Sanitize text input"""
    return re.sub(r'[<>]', '', text).strip()