"""
Carbon Footprint Prediction using Machine Learning
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
from datetime import datetime
import json

class CarbonPredictor:
    """Predict carbon footprint using ML"""
    
    def __init__(self):
        self.model = None
        self.label_encoders = {}
        self.feature_columns = []
        self.model_path = "data/ml_models/carbon_predictor.pkl"
        self.encoder_path = "data/ml_models/label_encoders.pkl"
        self.load_model()
    
    def load_model(self):
        """Load pre-trained model if exists"""
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
            else:
                self.model = None
            
            if os.path.exists(self.encoder_path):
                self.label_encoders = joblib.load(self.encoder_path)
            else:
                self.label_encoders = {}
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None
            self.label_encoders = {}
    
    def save_model(self):
        """Save trained model and encoders"""
        os.makedirs("data/ml_models", exist_ok=True)
        joblib.dump(self.model, self.model_path)
        joblib.dump(self.label_encoders, self.encoder_path)
    
    def get_all_categories(self):
        """Get all possible categories for encoding"""
        return {
            'transport_type': ['car', 'public_transport', 'bicycle', 'walking', 'electric_vehicle'],
            'electricity': ['low', 'medium', 'high'],
            'diet': ['omnivore', 'vegetarian', 'vegan', 'pescatarian'],
            'shopping': ['low', 'medium', 'high'],
            'location': ['Urban', 'Suburban', 'Rural']
        }
    
    def prepare_features(self, user_data, historical_data=None):
        """Prepare features for ML model with proper encoding"""
        features = []
        
        # Get all possible categories
        all_categories = self.get_all_categories()
        
        # Encode categorical variables with proper handling
        categories = ['transport_type', 'electricity', 'diet', 'shopping', 'location']
        
        for cat in categories:
            if cat in user_data:
                value = user_data[cat]
                # If encoder doesn't exist or value not seen before, fit with all categories
                if cat not in self.label_encoders:
                    self.label_encoders[cat] = LabelEncoder()
                    self.label_encoders[cat].fit(all_categories.get(cat, [value]))
                
                # If value is in known categories, transform it
                if value in self.label_encoders[cat].classes_:
                    encoded = self.label_encoders[cat].transform([value])[0]
                else:
                    # If value is new, add it to encoder
                    new_classes = list(self.label_encoders[cat].classes_) + [value]
                    self.label_encoders[cat].classes_ = np.array(new_classes)
                    encoded = self.label_encoders[cat].transform([value])[0]
                
                features.append(encoded)
            else:
                # Default value if category missing
                if cat not in self.label_encoders:
                    self.label_encoders[cat] = LabelEncoder()
                    self.label_encoders[cat].fit(all_categories.get(cat, ['medium']))
                features.append(0)
        
        # Numerical features
        features.append(float(user_data.get('weekly_distance', 100)))
        features.append(float(user_data.get('household_size', 2)))
        
        # Historical trend features (if available)
        if historical_data and len(historical_data) > 1:
            trend = self.calculate_trend(historical_data)
            features.append(float(trend))
        else:
            features.append(0.0)
        
        # Store feature columns for reference
        self.feature_columns = ['transport', 'electricity', 'diet', 'shopping', 'location', 
                               'weekly_distance', 'household_size', 'trend']
        
        return np.array(features).reshape(1, -1)
    
    def calculate_trend(self, historical_data):
        """Calculate trend from historical assessments"""
        if len(historical_data) < 2:
            return 0
        
        emissions = []
        for d in historical_data[-5:]:
            if 'footprint' in d and 'total' in d['footprint']:
                emissions.append(d['footprint']['total'])
        
        if len(emissions) < 2:
            return 0
        
        try:
            x = np.arange(len(emissions))
            slope = np.polyfit(x, emissions, 1)[0]
            return slope
        except:
            return 0
    
    def train_model(self, training_data):
        """Train the ML model"""
        if not training_data:
            print("No training data available")
            return {'mae': 0, 'r2': 0}
        
        X = []
        y = []
        
        # Get all categories for consistent encoding
        all_categories = self.get_all_categories()
        
        # Initialize encoders with all possible categories
        for cat, values in all_categories.items():
            if cat not in self.label_encoders:
                self.label_encoders[cat] = LabelEncoder()
                self.label_encoders[cat].fit(values)
        
        # Process each training sample
        for data in training_data:
            user_data = data['user_data']
            footprint = data['footprint']
            
            # Create feature vector
            features = []
            
            # Encode categorical variables
            categories = ['transport_type', 'electricity', 'diet', 'shopping', 'location']
            for cat in categories:
                if cat in user_data:
                    value = user_data[cat]
                    try:
                        encoded = self.label_encoders[cat].transform([value])[0]
                    except:
                        # If value not in encoder, add it
                        new_classes = list(self.label_encoders[cat].classes_) + [value]
                        self.label_encoders[cat].classes_ = np.array(new_classes)
                        encoded = self.label_encoders[cat].transform([value])[0]
                    features.append(encoded)
                else:
                    features.append(0)
            
            # Numerical features
            features.append(float(user_data.get('weekly_distance', 100)))
            features.append(float(user_data.get('household_size', 2)))
            
            # Trend (set to 0 for training samples without history)
            features.append(0.0)
            
            X.append(features)
            y.append(footprint['total'])
        
        X = np.array(X)
        y = np.array(y)
        
        # Store feature columns
        self.feature_columns = ['transport', 'electricity', 'diet', 'shopping', 'location', 
                               'weekly_distance', 'household_size', 'trend']
        
        # Split data
        if len(X) > 10:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        else:
            X_train, X_test, y_train, y_test = X, X, y, y
        
        # Train Random Forest
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_train, y_train)
        
        # Evaluate
        if len(X_test) > 0:
            y_pred = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
        else:
            y_pred = self.model.predict(X_train)
            mae = mean_absolute_error(y_train, y_pred)
            r2 = r2_score(y_train, y_pred)
        
        print(f"📊 Model trained successfully!")
        print(f"   - MAE: {mae:.2f} kg CO₂")
        print(f"   - R² Score: {r2:.3f}")
        
        self.save_model()
        return {'mae': mae, 'r2': r2}
    
    def predict_footprint(self, user_data, historical_data=None):
        """Predict carbon footprint for user"""
        if self.model is None:
            # Fallback to simple calculation if no ML model
            return self.fallback_prediction(user_data)
        
        try:
            features = self.prepare_features(user_data, historical_data)
            prediction = self.model.predict(features)[0]
            return max(0, round(prediction, 2))
        except Exception as e:
            print(f"Prediction error: {e}")
            return self.fallback_prediction(user_data)
    
    def fallback_prediction(self, user_data):
        """Fallback to calculator if ML fails"""
        try:
            from src.core.carbon_calculator import CarbonCalculator
            calc = CarbonCalculator()
            footprint = calc.calculate_footprint(user_data)
            return footprint['total']
        except:
            return 50.0  # Default fallback

    def predict_future_trend(self, historical_data, weeks=4):
        """Predict future carbon footprint trend"""
        if not historical_data or len(historical_data) < 3:
            return None
        
        emissions = []
        for d in historical_data[-10:]:
            if 'footprint' in d and 'total' in d['footprint']:
                emissions.append(d['footprint']['total'])
        
        if len(emissions) < 3:
            return None
        
        try:
            from sklearn.linear_model import LinearRegression
            x = np.arange(len(emissions)).reshape(-1, 1)
            y = np.array(emissions)
            
            model = LinearRegression()
            model.fit(x, y)
            
            # Predict future weeks
            future_x = np.arange(len(emissions), len(emissions) + weeks).reshape(-1, 1)
            future_predictions = model.predict(future_x)
            
            return {
                'current_trend': model.coef_[0],
                'predictions': [max(0, round(p, 2)) for p in future_predictions],
                'weeks': weeks
            }
        except:
            return None