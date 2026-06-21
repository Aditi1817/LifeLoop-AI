"""
ML-based Recommendation Engine for Personalized Suggestions
"""

import numpy as np
import random
from datetime import datetime

class RecommendationEngine:
    """AI-powered recommendation engine using ML"""
    
    def __init__(self):
        self.recommendations_db = self.load_recommendations()
    
    def load_recommendations(self):
        """Load pre-defined recommendations database"""
        return [
            {
                'id': 1,
                'category': 'Transport',
                'action': 'Switch to public transport 2 days/week',
                'impact': 8.4,
                'difficulty': 'Easy',
                'savings': 15,
                'tags': ['transport', 'public', 'commute']
            },
            {
                'id': 2,
                'category': 'Food',
                'action': 'Reduce meat consumption to 3 days/week',
                'impact': 12.0,
                'difficulty': 'Medium',
                'savings': 20,
                'tags': ['food', 'meat', 'diet']
            },
            {
                'id': 3,
                'category': 'Energy',
                'action': 'Switch to LED bulbs everywhere',
                'impact': 3.5,
                'difficulty': 'Easy',
                'savings': 8,
                'tags': ['energy', 'lighting', 'electricity']
            },
            {
                'id': 4,
                'category': 'Transport',
                'action': 'Carpool with colleagues 3 days/week',
                'impact': 10.5,
                'difficulty': 'Medium',
                'savings': 30,
                'tags': ['transport', 'carpool', 'commute']
            },
            {
                'id': 5,
                'category': 'Food',
                'action': 'Eat plant-based for 5 days/week',
                'impact': 18.0,
                'difficulty': 'Hard',
                'savings': 35,
                'tags': ['food', 'vegan', 'plant-based']
            },
            {
                'id': 6,
                'category': 'Energy',
                'action': 'Install smart thermostat',
                'impact': 6.0,
                'difficulty': 'Medium',
                'savings': 25,
                'tags': ['energy', 'smart', 'thermostat']
            },
            {
                'id': 7,
                'category': 'Shopping',
                'action': 'Buy second-hand clothes',
                'impact': 4.0,
                'difficulty': 'Easy',
                'savings': 40,
                'tags': ['shopping', 'clothes', 'sustainable']
            },
            {
                'id': 8,
                'category': 'Transport',
                'action': 'Bike for trips under 5km',
                'impact': 7.0,
                'difficulty': 'Easy',
                'savings': 12,
                'tags': ['transport', 'bike', 'exercise']
            },
            {
                'id': 9,
                'category': 'Food',
                'action': 'Meal prep to reduce food waste',
                'impact': 5.0,
                'difficulty': 'Easy',
                'savings': 25,
                'tags': ['food', 'mealprep', 'waste']
            },
            {
                'id': 10,
                'category': 'Energy',
                'action': 'Use energy-efficient appliances',
                'impact': 8.0,
                'difficulty': 'Medium',
                'savings': 30,
                'tags': ['energy', 'appliances', 'efficiency']
            },
            {
                'id': 11,
                'category': 'Transport',
                'action': 'Work from home 2 days/week',
                'impact': 15.0,
                'difficulty': 'Medium',
                'savings': 45,
                'tags': ['transport', 'workfromhome', 'commute']
            },
            {
                'id': 12,
                'category': 'Shopping',
                'action': 'Buy local produce and products',
                'impact': 3.0,
                'difficulty': 'Easy',
                'savings': 10,
                'tags': ['shopping', 'local', 'sustainable']
            }
        ]
    
    def get_user_profile_vector(self, user_data, footprint_data):
        """Create user profile vector for recommendation"""
        profile_tags = []
        
        # Add category weights based on footprint
        total = footprint_data['total']
        if total > 0:
            category_weights = {
                'Transport': footprint_data.get('transport', 0) / total,
                'Food': footprint_data.get('food', 0) / total,
                'Energy': footprint_data.get('energy', 0) / total,
                'Shopping': footprint_data.get('shopping', 0) / total
            }
            
            # Add weighted categories
            for category, weight in category_weights.items():
                if weight > 0.25:  # Significant contributor
                    profile_tags.append(category.lower())
        
        # Add lifestyle tags
        transport = user_data.get('transport_type', 'car')
        if transport == 'car':
            profile_tags.append('car')
        elif transport == 'public_transport':
            profile_tags.append('public')
        elif transport == 'bicycle' or transport == 'walking':
            profile_tags.append('active')
        
        # Diet preference
        diet = user_data.get('diet', 'omnivore')
        if diet == 'vegan' or diet == 'vegetarian':
            profile_tags.append('plant-based')
        else:
            profile_tags.append('meat')
        
        # Shopping habits
        shopping = user_data.get('shopping', 'medium')
        if shopping == 'high':
            profile_tags.append('frequent-shopper')
        else:
            profile_tags.append('minimal-shopper')
        
        return profile_tags
    
    def get_personalized_recommendations(self, user_data, footprint_data, historical_data=None):
        """Main method to get personalized recommendations"""
        
        # Get user profile tags
        user_tags = self.get_user_profile_vector(user_data, footprint_data)
        
        # Score each recommendation based on user profile
        scored_recs = []
        
        for rec in self.recommendations_db:
            score = 0
            
            # Match tags
            for tag in user_tags:
                if tag in rec['tags']:
                    score += 20
            
            # Prioritize categories where user has high impact
            total = footprint_data['total']
            if total > 0:
                category_weights = {
                    'Transport': footprint_data.get('transport', 0) / total,
                    'Food': footprint_data.get('food', 0) / total,
                    'Energy': footprint_data.get('energy', 0) / total,
                    'Shopping': footprint_data.get('shopping', 0) / total
                }
                
                if rec['category'] in category_weights:
                    score += category_weights[rec['category']] * 30
            
            # Preference for easier actions if user is new
            if historical_data and len(historical_data) < 3:
                if rec['difficulty'] == 'Easy':
                    score += 15
            
            # Preference for harder actions if user is experienced
            if historical_data and len(historical_data) > 5:
                if rec['difficulty'] == 'Hard':
                    score += 10
            
            # Random factor for diversity
            score += random.randint(0, 10)
            
            scored_recs.append((rec, score))
        
        # Sort by score descending
        scored_recs.sort(key=lambda x: x[1], reverse=True)
        
        # Get top 3 recommendations
        top_recs = []
        for rec, score in scored_recs[:3]:
            top_recs.append({
                'action': rec['action'],
                'co2_reduction': f"{rec['impact']} kg/week",
                'difficulty': rec['difficulty'],
                'savings': f"${rec['savings']}/week",
                'confidence': min(95, int(score))
            })
        
        return top_recs

    def get_recommendations_by_category(self, category, limit=3):
        """Get recommendations for a specific category"""
        category_recs = [rec for rec in self.recommendations_db if rec['category'] == category]
        random.shuffle(category_recs)
        
        recommendations = []
        for rec in category_recs[:limit]:
            recommendations.append({
                'action': rec['action'],
                'co2_reduction': f"{rec['impact']} kg/week",
                'difficulty': rec['difficulty'],
                'savings': f"${rec['savings']}/week",
                'confidence': random.randint(80, 95)
            })
        
        return recommendations