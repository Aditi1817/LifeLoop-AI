"""
Data models for LifeLoop AI
"""

from typing import Dict, List, Optional
from datetime import datetime

class User:
    def __init__(self, data: Dict):
        self.email = data.get('email')
        self.name = data.get('name')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.last_login = data.get('last_login')
        self.is_active = data.get('is_active', True)
        self.stats = data.get('stats', {})
        self.preferences = data.get('preferences', {})
        self.assessments = data.get('assessments', [])
    
    def to_dict(self) -> Dict:
        return {
            'email': self.email,
            'name': self.name,
            'password': self.password,
            'created_at': self.created_at,
            'last_login': self.last_login,
            'is_active': self.is_active,
            'stats': self.stats,
            'preferences': self.preferences,
            'assessments': self.assessments
        }

class Assessment:
    def __init__(self, data: Dict):
        self.data = data.get('data', {})
        self.footprint = data.get('footprint', {})
        self.date = data.get('date', datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        return {
            'data': self.data,
            'footprint': self.footprint,
            'date': self.date
        }