"""
Data Collection for ML Training
"""

import json
import os
from datetime import datetime
import numpy as np

class DataCollector:
    """Collect and prepare data for ML training"""
    
    def __init__(self):
        self.data_path = "data/ml_data/training_data.json"
        self.ensure_data_dir()
    
    def ensure_data_dir(self):
        """Create data directory if it doesn't exist"""
        os.makedirs("data/ml_data", exist_ok=True)
    
    def collect_user_data(self, user_data, footprint_data):
        """Collect user data for ML training"""
        training_data = self.load_training_data()
        
        data_point = {
            'user_data': user_data,
            'footprint': footprint_data,
            'timestamp': datetime.now().isoformat()
        }
        
        training_data.append(data_point)
        self.save_training_data(training_data)
    
    def load_training_data(self):
        """Load training data from file"""
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as f:
                return json.load(f)
        return []
    
    def save_training_data(self, data):
        """Save training data to file"""
        with open(self.data_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_training_data(self):
        """Get all training data"""
        return self.load_training_data()
    
    def generate_synthetic_data(self, num_samples=100):
        """Generate synthetic training data"""
        import random
        
        transport_types = ['car', 'public_transport', 'bicycle', 'walking', 'electric_vehicle']
        diets = ['omnivore', 'vegetarian', 'vegan', 'pescatarian']
        electricity_levels = ['low', 'medium', 'high']
        shopping_levels = ['low', 'medium', 'high']
        locations = ['Urban', 'Suburban', 'Rural']
        
        synthetic_data = []
        
        for _ in range(num_samples):
            transport = random.choice(transport_types)
            distance = random.randint(20, 300)
            diet = random.choice(diets)
            electricity = random.choice(electricity_levels)
            shopping = random.choice(shopping_levels)
            location = random.choice(locations)
            
            user_data = {
                'transport_type': transport,
                'weekly_distance': distance,
                'electricity': electricity,
                'diet': diet,
                'shopping': shopping,
                'location': location,
                'household_size': random.randint(1, 5)
            }
            
            # Calculate approximate footprint
            from src.core.carbon_calculator import CarbonCalculator
            calc = CarbonCalculator()
            footprint = calc.calculate_footprint(user_data)
            
            synthetic_data.append({
                'user_data': user_data,
                'footprint': footprint,
                'timestamp': datetime.now().isoformat(),
                'synthetic': True
            })
        
        return synthetic_data