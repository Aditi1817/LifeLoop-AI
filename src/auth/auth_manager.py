"""
Authentication Manager for LifeLoop AI
Handles user registration, login, session management
"""

import streamlit as st
import bcrypt
import jwt
import os
from datetime import datetime, timedelta
from typing import Dict, Optional
from src.data.database import Database
from src.utils.validators import validate_email, validate_password

class AuthManager:
    """Manages user authentication and session"""
    
    def __init__(self):
        self.db = Database()
        self.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this')
        
    def register_user(self, email: str, password: str, name: str) -> Dict:
        """Register a new user"""
        # Validate inputs
        if not validate_email(email):
            return {'success': False, 'error': 'Invalid email format'}
        
        if not validate_password(password):
            return {'success': False, 'error': 'Password must be at least 8 characters'}
        
        # Check if user exists
        if self.db.get_user_by_email(email):
            return {'success': False, 'error': 'User already exists'}
        
        # Hash password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Create user
        user_data = {
            'email': email,
            'password': hashed.decode('utf-8'),
            'name': name,
            'created_at': datetime.now().isoformat(),
            'last_login': None,
            'is_active': True,
            'preferences': {
                'theme': 'light',
                'notifications': True
            },
            'stats': {
                'total_assessments': 0,
                'total_co2_saved': 0,
                'achievements_unlocked': 0,
                'xp': 0,
                'level': 1
            }
        }
        
        if self.db.create_user(user_data):
            return {'success': True, 'message': 'Registration successful!'}
        
        return {'success': False, 'error': 'Registration failed'}
    
    def login_user(self, email: str, password: str) -> Dict:
        """Authenticate user and create session"""
        user = self.db.get_user_by_email(email)
        
        if not user:
            return {'success': False, 'error': 'User not found'}
        
        # Verify password
        try:
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                # Create session
                token = self.create_jwt(user['email'])
                
                # Update last login
                user['last_login'] = datetime.now().isoformat()
                self.db.update_user(user['email'], user)
                
                # Store in session
                st.session_state.user = user
                st.session_state.token = token
                st.session_state.logged_in = True
                
                return {'success': True, 'message': 'Login successful!'}
        except:
            pass
        
        return {'success': False, 'error': 'Invalid credentials'}
    
    def create_jwt(self, email: str) -> str:
        """Create JWT token for user"""
        payload = {
            'email': email,
            'exp': datetime.utcnow() + timedelta(hours=int(os.getenv('JWT_EXPIRATION_HOURS', 24)))
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')
    
    def verify_jwt(self, token: str) -> Optional[str]:
        """Verify JWT token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['email']
        except:
            return None
    
    def logout_user(self):
        """Logout user and clear session"""
        for key in ['user', 'token', 'logged_in']:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state.clear()
        
    def is_logged_in(self) -> bool:
        """Check if user is logged in"""
        if 'logged_in' in st.session_state and st.session_state.logged_in:
            if 'token' in st.session_state:
                email = self.verify_jwt(st.session_state.token)
                if email:
                    return True
        return False
    
    def get_current_user(self) -> Optional[Dict]:
        """Get current logged in user"""
        if self.is_logged_in():
            return st.session_state.user
        return None
    
    def update_user_stats(self, email: str, data: Dict):
        """Update user statistics"""
        user = self.db.get_user_by_email(email)
        if user:
            if 'stats' in user:
                user['stats'].update(data)
                # Check for level up
                xp = user['stats'].get('xp', 0)
                level = 1
                if xp >= 1000:
                    level = 5
                elif xp >= 500:
                    level = 4
                elif xp >= 200:
                    level = 3
                elif xp >= 50:
                    level = 2
                user['stats']['level'] = level
            else:
                user['stats'] = data
            self.db.update_user(email, user)
            if self.is_logged_in():
                st.session_state.user = user

    def reset_password(self, email: str, new_password: str) -> Dict:
        """Reset user password"""
        if not validate_password(new_password):
            return {'success': False, 'error': 'Invalid password format'}
        
        user = self.db.get_user_by_email(email)
        if not user:
            return {'success': False, 'error': 'User not found'}
        
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        user['password'] = hashed.decode('utf-8')
        
        if self.db.update_user(email, user):
            return {'success': True, 'message': 'Password updated successfully!'}
        
        return {'success': False, 'error': 'Password reset failed'}