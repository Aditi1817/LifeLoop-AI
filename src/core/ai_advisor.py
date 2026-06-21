"""
AI-powered sustainability advisor using Gemini API
"""

import google.generativeai as genai
import os
from typing import Dict, Any, List
import json

class AIAdvisor:
    """AI advisor for sustainability recommendations"""
    
    def __init__(self, api_key: str):
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
    
    def generate_recommendations(self, user_data: Dict[str, Any], footprint_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate personalized sustainability recommendations"""
        
        if not self.model:
            return self._get_fallback_recommendations(footprint_data)
        
        prompt = self._build_prompt(user_data, footprint_data)
        
        try:
            response = self.model.generate_content(prompt)
            return self._parse_recommendations(response.text)
        except:
            return self._get_fallback_recommendations(footprint_data)
    
    def _build_prompt(self, user_data: Dict[str, Any], footprint_data: Dict[str, Any]) -> str:
        categories = {
            'Transport': footprint_data.get('transport', 0),
            'Food': footprint_data.get('food', 0),
            'Energy': footprint_data.get('energy', 0),
            'Shopping': footprint_data.get('shopping', 0)
        }
        top_category = max(categories, key=categories.get)
        
        return f"""
        Generate 3 personalized recommendations to reduce carbon footprint.
        User: {user_data}
        Footprint: {footprint_data}
        Highest category: {top_category}
        Return JSON array with action, co2_reduction, difficulty, savings.
        """
    
    def _parse_recommendations(self, ai_response: str) -> List[Dict[str, Any]]:
        try:
            start_idx = ai_response.find('[')
            end_idx = ai_response.rfind(']') + 1
            if start_idx != -1 and end_idx != 0:
                json_str = ai_response[start_idx:end_idx]
                return json.loads(json_str)
        except:
            pass
        return self._get_fallback_recommendations({})
    
    def _get_fallback_recommendations(self, footprint_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        return [
            {"action": "Switch to public transport for 2 days per week", "co2_reduction": "8.4 kg/week", "difficulty": "Easy", "savings": "$15/week"},
            {"action": "Reduce meat consumption to 3 days per week", "co2_reduction": "12 kg/week", "difficulty": "Medium", "savings": "$20/week"},
            {"action": "Replace 5 light bulbs with LED bulbs", "co2_reduction": "3.5 kg/week", "difficulty": "Easy", "savings": "$8/week"}
        ]