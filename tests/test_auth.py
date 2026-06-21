"""
Unit tests for Authentication
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.auth.auth_manager import AuthManager
from src.utils.validators import validate_email, validate_password

class TestAuthManager(unittest.TestCase):
    """Test cases for AuthManager"""
    
    def setUp(self):
        self.auth_manager = AuthManager()
    
    def test_validate_email(self):
        """Test email validation"""
        self.assertTrue(validate_email('test@example.com'))
        self.assertTrue(validate_email('user.name@domain.co.uk'))
        self.assertFalse(validate_email('invalid-email'))
        self.assertFalse(validate_email('test@'))
        self.assertFalse(validate_email('@example.com'))
    
    def test_validate_password(self):
        """Test password validation"""
        self.assertTrue(validate_password('password123'))
        self.assertTrue(validate_password('SecurePass!@#123'))
        self.assertFalse(validate_password('short'))
        self.assertFalse(validate_password('1234567'))
    
    @patch('src.data.database.Database.get_user_by_email')
    def test_register_user_existing(self, mock_get_user):
        """Test registration with existing user"""
        mock_get_user.return_value = {'email': 'test@example.com'}
        
        result = self.auth_manager.register_user('test@example.com', 'password123', 'Test User')
        self.assertFalse(result['success'])
        self.assertEqual(result['error'], 'User already exists')
    
    @patch('src.data.database.Database.create_user')
    @patch('src.data.database.Database.get_user_by_email')
    def test_register_user_success(self, mock_get_user, mock_create_user):
        """Test successful registration"""
        mock_get_user.return_value = None
        mock_create_user.return_value = True
        
        result = self.auth_manager.register_user('new@example.com', 'password123', 'New User')
        self.assertTrue(result['success'])

class TestValidators(unittest.TestCase):
    """Test cases for validators"""
    
    def test_email_validation(self):
        """Test various email formats"""
        valid_emails = [
            'user@example.com',
            'user.name@domain.com',
            'user-name@domain.co.uk',
            'user_name@domain.io'
        ]
        
        invalid_emails = [
            'invalid',
            'user@',
            '@domain.com',
            'user@domain.',
            'user name@domain.com'
        ]
        
        for email in valid_emails:
            self.assertTrue(validate_email(email))
        
        for email in invalid_emails:
            self.assertFalse(validate_email(email))
    
    def test_password_validation(self):
        """Test password strength validation"""
        # Valid passwords (8+ characters)
        self.assertTrue(validate_password('password123'))
        self.assertTrue(validate_password('SecurePass!@#'))
        self.assertTrue(validate_password('12345678'))
        
        # Invalid passwords
        self.assertFalse(validate_password('short'))
        self.assertFalse(validate_password('1234567'))
        self.assertFalse(validate_password(''))

if __name__ == '__main__':
    unittest.main()