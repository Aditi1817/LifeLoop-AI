"""
User Clustering for Behavioral Analysis
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import joblib
import os

class UserClustering:
    """Cluster users based on behavior patterns"""
    
    def __init__(self):
        self.model = None
        self.scaler = None
        self.model_path = "data/ml_models/user_clusters.pkl"
        self.scaler_path = "data/ml_models/scaler.pkl"
        self.load_model()
    
    def load_model(self):
        """Load pre-trained clustering model"""
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
            if os.path.exists(self.scaler_path):
                self.scaler = joblib.load(self.scaler_path)
        except:
            self.model = None
            self.scaler = None
    
    def save_model(self):
        """Save clustering model"""
        os.makedirs("data/ml_models", exist_ok=True)
        joblib.dump(self.model, self.model_path)
        joblib.dump(self.scaler, self.scaler_path)
    
    def extract_features(self, user_data):
        """Extract features for clustering"""
        features = []
        
        # Transportation features
        transport_types = {'car': 0, 'public_transport': 1, 'bicycle': 2, 'walking': 3, 'electric_vehicle': 4}
        features.append(transport_types.get(user_data.get('transport_type', 'car'), 0))
        
        # Weekly distance (normalized)
        distance = user_data.get('weekly_distance', 100)
        features.append(distance / 500)  # Normalize to 0-1
        
        # Diet types
        diet_types = {'omnivore': 0, 'vegetarian': 1, 'vegan': 2, 'pescatarian': 3}
        features.append(diet_types.get(user_data.get('diet', 'omnivore'), 0))
        
        # Electricity usage
        electricity_levels = {'low': 0, 'medium': 1, 'high': 2}
        features.append(electricity_levels.get(user_data.get('electricity', 'medium'), 1))
        
        # Shopping habits
        shopping_levels = {'low': 0, 'medium': 1, 'high': 2}
        features.append(shopping_levels.get(user_data.get('shopping', 'medium'), 1))
        
        # Location
        location_types = {'Urban': 0, 'Suburban': 1, 'Rural': 2}
        features.append(location_types.get(user_data.get('location', 'Urban'), 0))
        
        # Household size
        features.append(user_data.get('household_size', 2))
        
        return np.array(features)
    
    def cluster_users(self, user_data_list, n_clusters=4):
        """Cluster users based on their data"""
        if len(user_data_list) < n_clusters:
            return None
        
        # Extract features for all users
        features = np.array([self.extract_features(user) for user in user_data_list])
        
        # Scale features
        self.scaler = StandardScaler()
        features_scaled = self.scaler.fit_transform(features)
        
        # Apply K-means clustering
        self.model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        clusters = self.model.fit_predict(features_scaled)
        
        self.save_model()
        
        return clusters
    
    def predict_cluster(self, user_data):
        """Predict which cluster a user belongs to"""
        if self.model is None or self.scaler is None:
            return None
        
        features = self.extract_features(user_data)
        features_scaled = self.scaler.transform(features.reshape(1, -1))
        cluster = self.model.predict(features_scaled)[0]
        
        return cluster
    
    def get_cluster_profile(self, cluster_id):
        """Get profile description for a cluster"""
        profiles = {
            0: "🌱 Eco-Conscious Beginner - Just starting sustainability journey",
            1: "🌿 Green Enthusiast - Actively making eco-friendly choices",
            2: "🌍 Eco Warrior - Highly committed to sustainability",
            3: "♻️ Sustainability Champion - Leading the way in green living"
        }
        return profiles.get(cluster_id, "🌱 Sustainability Explorer")
    
    def reduce_dimensions(self, features, n_components=2):
        """Reduce dimensions for visualization"""
        pca = PCA(n_components=n_components)
        features_reduced = pca.fit_transform(features)
        return features_reduced