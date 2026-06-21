"""
Unit tests for Carbon Calculator
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.carbon_calculator import CarbonCalculator

class TestCarbonCalculator(unittest.TestCase):
    """Test cases for CarbonCalculator"""
    
    def setUp(self):
        self.calculator = CarbonCalculator()
    
    def test_calculate_transport(self):
        """Test transport emissions calculation"""
        result = self.calculator.calculate_transport('car', 100)
        self.assertEqual(result, 21.0)
        
        result = self.calculator.calculate_transport('bicycle', 100)
        self.assertEqual(result, 0.0)
    
    def test_calculate_food(self):
        """Test food emissions calculation"""
        result = self.calculator.calculate_food('omnivore')
        self.assertEqual(result, 17.5)
        
        result = self.calculator.calculate_food('vegan')
        self.assertEqual(result, 8.4)
    
    def test_calculate_energy(self):
        """Test energy emissions calculation"""
        result = self.calculator.calculate_energy('low')
        self.assertEqual(result, 1.4)
        
        result = self.calculator.calculate_energy('high')
        self.assertEqual(result, 6.3)
    
    def test_calculate_eco_score(self):
        """Test eco score calculation"""
        score = self.calculator.calculate_eco_score(20)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
        
        # Test boundaries
        score = self.calculator.calculate_eco_score(0)
        self.assertEqual(score, 100)
        
        score = self.calculator.calculate_eco_score(200)
        self.assertEqual(score, 0)
    
    def test_calculate_footprint(self):
        """Test full footprint calculation"""
        user_data = {
            'transport_type': 'car',
            'weekly_distance': 100,
            'diet': 'omnivore',
            'electricity': 'medium',
            'shopping': 'medium'
        }
        
        result = self.calculator.calculate_footprint(user_data)
        
        self.assertIn('total', result)
        self.assertIn('transport', result)
        self.assertIn('food', result)
        self.assertIn('energy', result)
        self.assertIn('shopping', result)
        self.assertIn('eco_score', result)
        
        self.assertIsInstance(result['total'], float)
        self.assertIsInstance(result['eco_score'], int)

if __name__ == '__main__':
    unittest.main()