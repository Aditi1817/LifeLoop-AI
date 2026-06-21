"""
Gamification system for XP, levels, and achievements
"""

from typing import Dict, List

class GamificationManager:
    """Manage gamification features"""
    
    def __init__(self):
        self.achievements = self.load_achievements()
    
    def load_achievements(self) -> Dict:
        return {
            'first_assessment': {'name': '🌱 First Step', 'description': 'Complete your first carbon assessment', 'xp': 25},
            'carbon_saver': {'name': '💚 Carbon Saver', 'description': 'Reduce carbon footprint by 10%', 'xp': 50},
            'eco_warrior': {'name': '🌟 Eco Warrior', 'description': 'Complete 5 assessments', 'xp': 100},
            'sustainability_champion': {'name': '🏆 Sustainability Champion', 'description': 'Reach level 5', 'xp': 200}
        }
    
    def calculate_xp(self, eco_score: int) -> int:
        """Calculate XP earned from assessment"""
        if eco_score >= 80:
            return 100
        elif eco_score >= 60:
            return 75
        elif eco_score >= 40:
            return 50
        else:
            return 25
    
    def check_achievements(self, user_stats: Dict) -> List[str]:
        """Check and unlock achievements"""
        unlocked = []
        if user_stats.get('total_assessments', 0) >= 1:
            unlocked.append('first_assessment')
        if user_stats.get('total_assessments', 0) >= 5:
            unlocked.append('eco_warrior')
        if user_stats.get('level', 1) >= 5:
            unlocked.append('sustainability_champion')
        return unlocked
    
    def get_level(self, xp: int) -> int:
        """Calculate level based on XP"""
        if xp >= 1000:
            return 5
        elif xp >= 500:
            return 4
        elif xp >= 200:
            return 3
        elif xp >= 50:
            return 2
        else:
            return 1