"""
Security utilities for LifeLoop AI
"""

import hashlib
import secrets
import re
from typing import Optional

class Security:
    """Security utilities"""
    
    @staticmethod
    def generate_csrf_token() -> str:
        """Generate CSRF token"""
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """Sanitize user input"""
        text = re.sub(r'[<>]', '', text)
        return text.strip()
    
    @staticmethod
    def validate_session() -> bool:
        """Validate current session"""
        import streamlit as st
        if 'logged_in' not in st.session_state:
            return False
        if not st.session_state.logged_in:
            return False
        return True