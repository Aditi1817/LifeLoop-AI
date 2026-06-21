"""
Train ML Models for LifeLoop AI
Run this script to train all machine learning models
"""

import sys
import os
import json
import numpy as np
import pandas as pd
from datetime import datetime
import random

# Add src to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ml.carbon_predictor import CarbonPredictor
from src.ml.user_clustering import UserClustering
from src.ml.recommendation_engine import RecommendationEngine
from src.ml.data_collector import DataCollector
from src.core.carbon_calculator import CarbonCalculator

def generate_synthetic_training_data(num_samples=200):
    """Generate synthetic training data for ML models"""
    
    print("📊 Generating synthetic training data...")
    
    transport_types = ['car', 'public_transport', 'bicycle', 'walking', 'electric_vehicle']
    diets = ['omnivore', 'vegetarian', 'vegan', 'pescatarian']
    electricity_levels = ['low', 'medium', 'high']
    shopping_levels = ['low', 'medium', 'high']
    locations = ['Urban', 'Suburban', 'Rural']
    
    synthetic_data = []
    calc = CarbonCalculator()
    
    for i in range(num_samples):
        # Generate random user data
        transport = random.choice(transport_types)
        distance = random.randint(10, 400)
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
            'household_size': random.randint(1, 6)
        }
        
        # Calculate footprint using the calculator
        footprint = calc.calculate_footprint(user_data)
        
        # Add some randomness to make it more realistic
        noise = random.uniform(-0.5, 0.5)
        footprint['total'] = max(0, footprint['total'] + noise)
        
        synthetic_data.append({
            'user_data': user_data,
            'footprint': footprint,
            'timestamp': datetime.now().isoformat(),
            'synthetic': True
        })
    
    print(f"   ✅ Generated {len(synthetic_data)} synthetic samples")
    return synthetic_data

def load_real_training_data():
    """Load real user data from database if available"""
    
    real_data = []
    data_path = "data/ml_data/training_data.json"
    
    if os.path.exists(data_path):
        try:
            with open(data_path, 'r') as f:
                real_data = json.load(f)
            print(f"   ✅ Loaded {len(real_data)} real data points")
        except:
            print("   ⚠️ Could not load real data, using synthetic only")
    
    return real_data

def train_carbon_predictor(training_data):
    """Train the carbon footprint predictor model"""
    
    print("\n🔄 Training Carbon Predictor...")
    
    predictor = CarbonPredictor()
    
    # Prepare training data
    train_data = []
    for data in training_data:
        train_data.append({
            'user_data': data['user_data'],
            'footprint': data['footprint']
        })
    
    if len(train_data) < 10:
        print("   ⚠️ Not enough training data! Need at least 10 samples.")
        print("   💡 Generating more synthetic data...")
        
        # Generate more synthetic data
        extra_data = generate_synthetic_training_data(100)
        for data in extra_data:
            train_data.append({
                'user_data': data['user_data'],
                'footprint': data['footprint']
            })
    
    try:
        result = predictor.train_model(train_data)
        print(f"   ✅ Predictor trained successfully!")
        print(f"      - MAE: {result['mae']:.2f} kg CO₂")
        print(f"      - R² Score: {result['r2']:.3f}")
        return True
    except Exception as e:
        print(f"   ❌ Error training predictor: {e}")
        return False

def train_user_clustering(training_data):
    """Train the user clustering model"""
    
    print("\n🔄 Training User Clustering...")
    
    clusterer = UserClustering()
    
    # Prepare user data for clustering
    user_data_list = []
    for data in training_data:
        user_data_list.append(data['user_data'])
    
    if len(user_data_list) < 10:
        print("   ⚠️ Not enough user data for clustering!")
        print("   💡 Generating more synthetic data...")
        
        extra_data = generate_synthetic_training_data(50)
        for data in extra_data:
            user_data_list.append(data['user_data'])
    
    try:
        clusters = clusterer.cluster_users(user_data_list, n_clusters=4)
        
        if clusters is not None:
            unique_clusters = len(set(clusters))
            print(f"   ✅ Clustering complete!")
            print(f"      - Found {unique_clusters} clusters")
            print(f"      - Users per cluster:")
            
            for i in range(unique_clusters):
                count = sum(1 for c in clusters if c == i)
                print(f"        Cluster {i}: {count} users")
            return True
        else:
            print("   ❌ Clustering failed!")
            return False
    except Exception as e:
        print(f"   ❌ Error in clustering: {e}")
        return False

def test_models():
    """Test trained models with sample data"""
    
    print("\n🧪 Testing trained models...")
    
    test_user = {
        'transport_type': 'car',
        'weekly_distance': 150,
        'electricity': 'medium',
        'diet': 'omnivore',
        'shopping': 'medium',
        'location': 'Urban',
        'household_size': 2
    }
    
    # Test Carbon Predictor
    try:
        predictor = CarbonPredictor()
        prediction = predictor.predict_footprint(test_user)
        print(f"   ✅ Predictor test: {prediction} kg CO₂")
    except Exception as e:
        print(f"   ❌ Predictor test failed: {e}")
    
    # Test User Clustering
    try:
        clusterer = UserClustering()
        cluster = clusterer.predict_cluster(test_user)
        if cluster is not None:
            profile = clusterer.get_cluster_profile(cluster)
            print(f"   ✅ Clustering test: Cluster {cluster} - {profile}")
        else:
            print("   ⚠️ Clustering test: No cluster predicted")
    except Exception as e:
        print(f"   ❌ Clustering test failed: {e}")

def save_model_summary():
    """Save model training summary"""
    
    summary = {
        'timestamp': datetime.now().isoformat(),
        'models_trained': ['carbon_predictor', 'user_clustering'],
        'status': 'completed',
        'version': '2.0.0'
    }
    
    os.makedirs("data/ml_models", exist_ok=True)
    
    with open("data/ml_models/training_summary.json", 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("\n📁 Model summary saved to data/ml_models/training_summary.json")

def main():
    """Main training function"""
    
    print("=" * 60)
    print("🌱 LifeLoop AI - Machine Learning Model Training")
    print("=" * 60)
    print(f"📅 Training started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Step 1: Collect training data
    print("\n📊 Step 1: Collecting training data...")
    
    # Load real data
    real_data = load_real_training_data()
    
    # Generate synthetic data
    synthetic_data = generate_synthetic_training_data(150)
    
    # Combine data
    training_data = real_data + synthetic_data
    print(f"   📊 Total training samples: {len(training_data)}")
    print(f"      - Real data: {len(real_data)}")
    print(f"      - Synthetic data: {len(synthetic_data)}")
    
    # Step 2: Train Carbon Predictor
    print("\n🎯 Step 2: Training Carbon Predictor...")
    predictor_success = train_carbon_predictor(training_data)
    
    # Step 3: Train User Clustering
    print("\n🎯 Step 3: Training User Clustering...")
    clustering_success = train_user_clustering(training_data)
    
    # Step 4: Test models
    if predictor_success or clustering_success:
        test_models()
    
    # Step 5: Save summary
    if predictor_success or clustering_success:
        save_model_summary()
    
    # Final status
    print("\n" + "=" * 60)
    print("📊 Training Summary")
    print("=" * 60)
    print(f"✅ Carbon Predictor: {'✅ Trained' if predictor_success else '❌ Failed'}")
    print(f"✅ User Clustering: {'✅ Trained' if clustering_success else '❌ Failed'}")
    print(f"📁 Models saved to: data/ml_models/")
    print("=" * 60)
    
    if predictor_success and clustering_success:
        print("\n🎉 All models trained successfully!")
        print("🚀 You can now run: streamlit run app.py")
        print("   And navigate to '🧠 ML Insights' page")
    else:
        print("\n⚠️ Some models failed to train.")
        print("💡 Make sure you have sufficient training data.")
        print("   Try increasing the number of synthetic samples.")
    
    print("\n✅ Training complete!")

if __name__ == "__main__":
    main()