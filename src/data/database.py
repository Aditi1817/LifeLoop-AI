"""
JSON-based Database for LifeLoop AI
"""

import json
import os
from typing import Dict, Optional, List
from datetime import datetime

class Database:
    """Simple JSON database for user data"""
    
    def __init__(self):
        self.data_dir = "data/users"
        self.ensure_data_dir()
    
    def ensure_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def get_user_path(self, email: str) -> str:
        return os.path.join(self.data_dir, f"{email.replace('@', '_at_')}.json")
    
    def create_user(self, user_data: Dict) -> bool:
        try:
            email = user_data.get('email')
            if not email:
                return False
            
            path = self.get_user_path(email)
            if os.path.exists(path):
                return False
            
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(user_data, f, indent=2, ensure_ascii=False)
            return True
        except:
            return False
    
    def get_user_by_email(self, email: str) -> Optional[Dict]:
        try:
            path = self.get_user_path(email)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return None
    
    def update_user(self, email: str, user_data: Dict) -> bool:
        try:
            path = self.get_user_path(email)
            if os.path.exists(path):
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(user_data, f, indent=2, ensure_ascii=False)
                return True
        except:
            pass
        return False
    
    def delete_user(self, email: str) -> bool:
        try:
            path = self.get_user_path(email)
            if os.path.exists(path):
                os.remove(path)
                return True
        except:
            pass
        return False
    
    def save_assessment(self, email: str, assessment_data: Dict) -> bool:
        user = self.get_user_by_email(email)
        if not user:
            return False
        
        if 'assessments' not in user:
            user['assessments'] = []
        
        user['assessments'].append(assessment_data)
        
        if 'stats' in user:
            user['stats']['total_assessments'] = len(user['assessments'])
        
        return self.update_user(email, user)
    
    def get_assessments(self, email: str) -> List[Dict]:
        user = self.get_user_by_email(email)
        if user and 'assessments' in user:
            return user['assessments']
        return []