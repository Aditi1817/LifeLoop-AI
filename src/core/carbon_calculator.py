"""
Carbon footprint calculator module
"""

import json
import os
from typing import Dict, Any

class CarbonCalculator:
    """Calculate carbon footprint based on user inputs"""
    
    def __init__(self):
        self.load_factors()
    
    def load_factors(self):
        """Load carbon emission factors from JSON file"""
        try:
            with open('data/carbon_factors.json', 'r') as f:
                self.factors = json.load(f)
        except FileNotFoundError:
            self.factors = {
                "carbon_per_km": {"car": 0.21, "public_transport": 0.08, "bicycle": 0, "walking": 0, "electric_vehicle": 0.12},
                "diet": {"omnivore": 2.5, "vegetarian": 1.8, "vegan": 1.2, "pescatarian": 2.0},
                "electricity": {"low": 0.2, "medium": 0.5, "high": 0.9},
                "shopping": {"low": 0.3, "medium": 0.7, "high": 1.2}
            }
    
    def calculate_footprint(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate carbon footprint breakdown"""
        transport = self.calculate_transport(user_data.get('transport_type', 'car'), user_data.get('weekly_distance', 100))
        food = self.calculate_food(user_data.get('diet', 'omnivore'))
        energy = self.calculate_energy(user_data.get('electricity', 'medium'))
        shopping = self.calculate_shopping(user_data.get('shopping', 'medium'))
        
        total = transport + food + energy + shopping
        
        return {
            'total': round(total, 2),
            'transport': round(transport, 2),
            'food': round(food, 2),
            'energy': round(energy, 2),
            'shopping': round(shopping, 2),
            'eco_score': self.calculate_eco_score(total)
        }
    
    def calculate_transport(self, transport_type: str, weekly_distance: float) -> float:
        carbon_per_km = self.factors['carbon_per_km'].get(transport_type, 0.15)
        return weekly_distance * carbon_per_km
    
    def calculate_food(self, diet: str) -> float:
        base_factor = self.factors['diet'].get(diet, 2.5)
        return base_factor * 7
    
    def calculate_energy(self, electricity_usage: str) -> float:
        factor = self.factors['electricity'].get(electricity_usage, 0.5)
        return factor * 7
    
    def calculate_shopping(self, shopping_habit: str) -> float:
        factor = self.factors['shopping'].get(shopping_habit, 0.7)
        return factor * 7
    
    def calculate_eco_score(self, total_footprint: float) -> int:
        score = max(0, min(100, int(100 - (total_footprint / 2))))
        return score
    
    def get_previous_footprint(self, current_total: float) -> float:
        return round(current_total * 1.15, 2)

    def get_reduction_percentage(self, current: float, previous: float) -> float:
        if previous == 0:
            return 0
        reduction = ((previous - current) / previous) * 100
        return round(max(-100, min(100, reduction)), 1)