"""
Pre-defined recommendations and goal management
"""

from typing import List, Dict, Any

class GoalManager:
    """Manage weekly sustainability goals"""
    
    def __init__(self):
        self.goals = self.get_default_goals()
    
    def get_default_goals(self) -> List[Dict[str, Any]]:
        return [
            {"id": 1, "title": "🚶 Walk More", "description": "Walk for trips under 2km instead of driving", "co2_saved": "3.5 kg", "difficulty": "Easy", "completed": False, "xp": 50},
            {"id": 2, "title": "🥗 Meat-Free Challenge", "description": "Go meatless for 3 days this week", "co2_saved": "8 kg", "difficulty": "Medium", "completed": False, "xp": 100},
            {"id": 3, "title": "💡 Energy Saver", "description": "Turn off lights and unplug devices", "co2_saved": "2.5 kg", "difficulty": "Easy", "completed": False, "xp": 40},
            {"id": 4, "title": "🛍️ Shop Mindfully", "description": "Avoid single-use plastics", "co2_saved": "4 kg", "difficulty": "Easy", "completed": False, "xp": 60},
            {"id": 5, "title": "🚌 Public Transport Week", "description": "Use public transport for 3 trips", "co2_saved": "10 kg", "difficulty": "Medium", "completed": False, "xp": 120},
            {"id": 6, "title": "♻️ Zero Food Waste", "description": "Plan meals and use all ingredients", "co2_saved": "5 kg", "difficulty": "Medium", "completed": False, "xp": 80}
        ]
    
    def get_weekly_goals(self) -> List[Dict[str, Any]]:
        return self.goals
    
    def complete_goal(self, goal_id: int) -> bool:
        for goal in self.goals:
            if goal["id"] == goal_id and not goal["completed"]:
                goal["completed"] = True
                return True
        return False
    
    def get_progress(self) -> Dict[str, Any]:
        completed = sum(1 for goal in self.goals if goal["completed"])
        total = len(self.goals)
        total_xp = sum(goal["xp"] for goal in self.goals if goal["completed"])
        return {"completed": completed, "total": total, "percentage": (completed / total) * 100 if total > 0 else 0, "total_xp": total_xp}
    
    def get_achievements(self) -> List[str]:
        achievements = []
        completed_count = sum(1 for goal in self.goals if goal["completed"])
        if completed_count >= 1:
            achievements.append("🌱 Green Beginner")
        if completed_count >= 3:
            achievements.append("🌟 Eco Warrior")
        if completed_count >= 6:
            achievements.append("🏆 Sustainability Champion")
        return achievements