"""
LifeLoop AI - Carbon Theme Edition
Professional Hackathon Ready Design with Unique Carbon Aesthetic
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import os
import random
import base64
from dotenv import load_dotenv

# Import modules
from src.auth.auth_manager import AuthManager
from src.core.carbon_calculator import CarbonCalculator
from src.core.ai_advisor import AIAdvisor
from src.core.recommendations import GoalManager
from src.core.gamification import GamificationManager
from src.data.database import Database
from src.utils.validators import validate_email, validate_password

# ML imports
from src.ml.carbon_predictor import CarbonPredictor
from src.ml.user_clustering import UserClustering
from src.ml.recommendation_engine import RecommendationEngine
from src.ml.data_collector import DataCollector

# Load environment
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="LifeLoop AI | Carbon Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============ PROFESSIONAL CARBON THEME CSS ============
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:400,500,600,700,800,900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Space Grotesk', 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Carbon Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0a1628 0%, #1a2a3a 30%, #2d4a4a 60%, #3d6b5e 100%);
        background-attachment: fixed;
    }
    
    /* Premium Glass Cards */
    .glass-card {
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 30px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        color: #e8f0f0;
    }
    
    .glass-card:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 30px 80px rgba(0,0,0,0.5);
        border-color: rgba(100, 200, 180, 0.2);
    }
    
    .glass-card h1, .glass-card h2, .glass-card h3 {
        color: #e8f0f0 !important;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .glass-card p {
        color: rgba(232, 240, 240, 0.85) !important;
    }
    
    /* Carbon Stat Cards */
    .stat-card {
        background: linear-gradient(145deg, rgba(20, 40, 50, 0.8), rgba(10, 30, 40, 0.9));
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid rgba(100, 200, 180, 0.15);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at center, rgba(100, 200, 180, 0.03), transparent 70%);
        animation: rotateGlow 20s linear infinite;
    }
    
    @keyframes rotateGlow {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .stat-card:hover {
        transform: translateY(-8px) scale(1.03);
        border-color: rgba(100, 200, 180, 0.4);
        box-shadow: 0 20px 50px rgba(0,0,0,0.4);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #64c8b4, #4aa8a0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px rgba(100, 200, 180, 0.2);
        position: relative;
        z-index: 1;
    }
    
    .stat-label {
        color: rgba(232, 240, 240, 0.8);
        font-weight: 500;
        margin-top: 5px;
        font-size: 0.95rem;
        position: relative;
        z-index: 1;
    }
    
    .stat-icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
    }
    
    /* Premium Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #64c8b4, #4aa8a0);
        color: #0a1628;
        border: none;
        border-radius: 50px;
        padding: 14px 32px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 5px 25px rgba(100, 200, 180, 0.3);
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 40px rgba(100, 200, 180, 0.5);
        background: linear-gradient(135deg, #7dd4c0, #5ab8b0);
    }
    
    .stButton > button:active {
        transform: scale(0.97);
    }
    
    /* Navigation Buttons - EQUAL SIZE FIX */
    .nav-container {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        margin: 10px 0;
    }
    
    .nav-container .stButton {
        width: 100%;
    }
    
    .nav-container .stButton > button {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 14px 8px;
        color: rgba(232, 240, 240, 0.7);
        font-weight: 600;
        font-size: 0.85rem;
        min-height: 75px;
        height: 75px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        text-transform: none;
        letter-spacing: normal;
        box-shadow: none;
        background: rgba(255,255,255,0.05);
    }
    
    .nav-container .stButton > button:hover {
        background: rgba(255,255,255,0.12);
        color: #e8f0f0;
        transform: translateY(-3px);
        border-color: rgba(100, 200, 180, 0.3);
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    }
    
    .nav-container .stButton > button:active {
        transform: scale(0.97);
    }
    
    /* Active state for nav buttons */
    .nav-btn-active {
        background: linear-gradient(135deg, rgba(100, 200, 180, 0.25), rgba(74, 168, 160, 0.15)) !important;
        border-color: #64c8b4 !important;
        color: #e8f0f0 !important;
        box-shadow: 0 5px 25px rgba(100, 200, 180, 0.15) !important;
    }
    
    @media (max-width: 768px) {
        .nav-container {
            grid-template-columns: repeat(4, 1fr);
            gap: 5px;
        }
        .nav-container .stButton > button {
            font-size: 0.75rem;
            min-height: 60px;
            height: 60px;
            padding: 8px 4px;
        }
    }
    
    @media (max-width: 480px) {
        .nav-container {
            grid-template-columns: repeat(3, 1fr);
        }
        .nav-container .stButton > button {
            font-size: 0.7rem;
            min-height: 55px;
            height: 55px;
            padding: 6px 3px;
        }
    }
    
    /* Auth Container */
    .auth-container {
        max-width: 480px;
        margin: 0 auto;
        padding: 45px;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border-radius: 30px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 30px 80px rgba(0,0,0,0.4);
    }
    
    .auth-container h3 {
        color: #e8f0f0 !important;
        font-weight: 700;
    }
    
    .auth-container label {
        color: rgba(232, 240, 240, 0.8) !important;
        font-weight: 500;
    }
    
    .auth-container input {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 14px 18px;
        border: 1px solid rgba(255,255,255,0.08);
        width: 100%;
        font-size: 1rem;
        color: #e8f0f0;
        transition: all 0.3s ease;
    }
    
    .auth-container input:focus {
        border-color: #64c8b4;
        box-shadow: 0 0 0 4px rgba(100, 200, 180, 0.1);
        outline: none;
        background: rgba(255,255,255,0.12);
    }
    
    .auth-container input::placeholder {
        color: rgba(232, 240, 240, 0.4);
    }
    
    .auth-container .stButton > button {
        width: 100%;
        padding: 16px;
        font-size: 1.1rem;
        margin-top: 10px;
    }
    
    /* Carbon Badge */
    .carbon-badge {
        background: linear-gradient(135deg, rgba(100, 200, 180, 0.2), rgba(74, 168, 160, 0.1));
        border: 1px solid rgba(100, 200, 180, 0.2);
        border-radius: 50px;
        padding: 10px 24px;
        display: inline-block;
        font-weight: 700;
        font-size: 0.85rem;
        color: #64c8b4;
        backdrop-filter: blur(10px);
    }
    
    /* Page Indicator */
    .page-indicator {
        background: linear-gradient(135deg, rgba(100, 200, 180, 0.15), rgba(74, 168, 160, 0.05));
        border: 1px solid rgba(100, 200, 180, 0.15);
        color: #e8f0f0;
        padding: 10px 28px;
        border-radius: 50px;
        display: inline-block;
        font-weight: 600;
        font-size: 0.9rem;
        backdrop-filter: blur(10px);
    }
    
    /* Carbon Footprint Animation */
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(100, 200, 180, 0.1); }
        50% { box-shadow: 0 0 40px rgba(100, 200, 180, 0.2); }
    }
    
    .pulse-glow {
        animation: pulseGlow 3s ease-in-out infinite;
    }
    
    /* Floating Animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
    }
    
    .float-animation {
        animation: float 4s ease-in-out infinite;
    }
    
    /* Slide Up Animation */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .slide-up {
        animation: slideUp 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }
    
    /* Feature Cards */
    .feature-card {
        background: rgba(255,255,255,0.04);
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.06);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
    }
    
    .feature-card:hover {
        background: rgba(255,255,255,0.08);
        transform: translateY(-8px);
        border-color: rgba(100, 200, 180, 0.2);
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
    }
    
    .feature-card h4 {
        color: #e8f0f0 !important;
        margin-top: 15px;
        font-weight: 600;
    }
    
    .feature-card p {
        color: rgba(232, 240, 240, 0.7) !important;
        font-size: 0.9rem;
        margin-top: 5px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.03);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #64c8b4, #4aa8a0);
        border-radius: 10px;
    }
    
    /* Alerts */
    .stAlert {
        border-radius: 14px;
        font-weight: 500;
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.08);
        color: #e8f0f0 !important;
    }
    
    .stSuccess {
        background: rgba(100, 200, 180, 0.1) !important;
        border-left: 4px solid #64c8b4 !important;
        color: #e8f0f0 !important;
    }
    
    .stInfo {
        background: rgba(100, 200, 180, 0.05) !important;
        border-left: 4px solid #4aa8a0 !important;
        color: #e8f0f0 !important;
    }
    
    /* Form Elements */
    .stSelectbox label, .stSlider label, .stNumberInput label {
        color: rgba(232, 240, 240, 0.85) !important;
        font-weight: 600 !important;
    }
    
    .stSelectbox > div > div, .stNumberInput > div > div {
        background: rgba(255,255,255,0.06);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
        color: #e8f0f0;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #4aa8a0, #64c8b4);
    }
    
    .stSlider > div > div > div > div {
        background: #64c8b4 !important;
        border: 2px solid #4aa8a0 !important;
        box-shadow: 0 0 20px rgba(100, 200, 180, 0.3);
    }
    
    /* Metrics */
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.04);
        padding: 18px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.06);
    }
    
    div[data-testid="stMetric"] label {
        color: rgba(232, 240, 240, 0.7) !important;
        font-weight: 500;
    }
    
    div[data-testid="stMetric"] div {
        color: #64c8b4 !important;
        font-weight: 800;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #4aa8a0, #64c8b4) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.04);
        border-radius: 12px;
        padding: 10px 22px;
        color: rgba(232, 240, 240, 0.6);
        font-weight: 500;
        border: 1px solid rgba(255,255,255,0.06);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.08);
        color: #e8f0f0;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, rgba(100, 200, 180, 0.2), rgba(74, 168, 160, 0.1));
        color: #e8f0f0;
        border-color: #64c8b4;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .stat-number { font-size: 2rem; }
        .glass-card { padding: 20px; }
        .auth-container { padding: 25px; margin: 10px; }
        .stButton > button { padding: 10px 20px; font-size: 0.9rem; }
    }
</style>
""", unsafe_allow_html=True)

# ============ HEADER WITH CARBON THEME ============
def render_header():
    """Render premium header with carbon theme"""
    
    col1, col2, col3 = st.columns([2, 1.2, 0.8])
    
    with col1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 55px; animation: float 4s ease-in-out infinite;">🌍</div>
            <div>
                <h1 style="color: #e8f0f0; margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">
                    <span style="background: linear-gradient(135deg, #64c8b4, #4aa8a0); 
                                 -webkit-background-clip: text; 
                                 -webkit-text-fill-color: transparent;">
                        LifeLoop AI
                    </span>
                </h1>
                <p style="color: rgba(232, 240, 240, 0.6); margin: 0; font-size: 0.9rem; letter-spacing: 1px;">
                    CARBON FOOTPRINT TRACKER
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 12px 20px; 
                    text-align: center; border: 1px solid rgba(255,255,255,0.06);">
            <div style="color: rgba(232, 240, 240, 0.6); font-size: 0.8rem; letter-spacing: 2px;">
                CARBON WARRIOR
            </div>
            <div style="color: #64c8b4; font-weight: 800; font-size: 1.1rem;">
                🌱 Make Every Choice Count
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
            auth_manager.logout_user()
            st.session_state.registration_complete = False
            st.rerun()
    
    st.markdown("---")

# ============ INITIALIZE ============
auth_manager = AuthManager()
db = Database()
calculator = CarbonCalculator()
gamification = GamificationManager()

# Initialize ML components
try:
    carbon_predictor = CarbonPredictor()
    user_clustering = UserClustering()
    recommendation_engine = RecommendationEngine()
    data_collector = DataCollector()
    ml_initialized = True
except:
    carbon_predictor = None
    user_clustering = None
    recommendation_engine = None
    data_collector = None
    ml_initialized = False

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
ai_advisor = AIAdvisor(api_key) if api_key else None

# ============ SESSION STATE ============
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'show_toast' not in st.session_state:
    st.session_state.show_toast = False
if 'toast_message' not in st.session_state:
    st.session_state.toast_message = ""
if 'registration_complete' not in st.session_state:
    st.session_state.registration_complete = False
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'assessment_data' not in st.session_state:
    st.session_state.assessment_data = None
if 'assessment_user' not in st.session_state:
    st.session_state.assessment_user = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'ml_recommendations' not in st.session_state:
    st.session_state.ml_recommendations = None

# ============ TOAST NOTIFICATION ============
def show_toast(message):
    st.session_state.show_toast = True
    st.session_state.toast_message = message

# ============ AUTHENTICATION UI ============
def show_auth_page():
    """Display authentication page with login/register"""
    
    if st.session_state.registration_complete:
        st.markdown("""
        <div style="text-align: center; padding: 15px; margin-bottom: 20px;">
            <div style="background: rgba(100,200,180,0.1); border-radius: 16px; padding: 15px; border: 1px solid rgba(100,200,180,0.2);">
                <span style="font-size: 24px;">✅</span>
                <span style="color: #e8f0f0; font-weight: 600; margin-left: 10px;">
                    Registration successful! Please login to continue.
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <div style="font-size: 80px; animation: float 4s ease-in-out infinite;">🌍</div>
        <h1 style="color: #e8f0f0; font-size: 3.5rem; font-weight: 900; margin: 10px 0; letter-spacing: -2px;">
            <span style="background: linear-gradient(135deg, #64c8b4, #4aa8a0); 
                         -webkit-background-clip: text; 
                         -webkit-text-fill-color: transparent;">
                LifeLoop AI
            </span>
        </h1>
        <p style="color: rgba(232, 240, 240, 0.6); font-size: 1.2rem; letter-spacing: 2px;">
            TRACK • REDUCE • SUSTAIN
        </p>
        <p style="color: rgba(232, 240, 240, 0.4); font-size: 0.9rem; margin-top: 5px;">
            Your Intelligent Carbon Footprint Companion
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
        
        with tab1:
            st.markdown('<div class="auth-container">', unsafe_allow_html=True)
            st.markdown("### Welcome Back 👋")
            st.markdown("<p style='color: rgba(232,240,240,0.6);'>Login to access your sustainability dashboard</p>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            with st.form("login_form"):
                email = st.text_input("📧 Email Address", placeholder="your@email.com")
                password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
                
                if st.form_submit_button("🚀 Login", use_container_width=True):
                    if email and password:
                        result = auth_manager.login_user(email, password)
                        if result['success']:
                            st.session_state.registration_complete = False
                            st.success(result['message'])
                            show_toast("🎉 Welcome back! Let's save the planet!")
                            st.rerun()
                        else:
                            st.error(result['error'])
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with tab2:
            st.markdown('<div class="auth-container">', unsafe_allow_html=True)
            st.markdown("### Create Account 🌟")
            st.markdown("<p style='color: rgba(232,240,240,0.6);'>Join the movement and start tracking your carbon footprint</p>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            with st.form("register_form"):
                name = st.text_input("👤 Full Name", placeholder="Your full name")
                email = st.text_input("📧 Email Address", placeholder="your@email.com")
                password = st.text_input("🔒 Password", type="password", placeholder="Min 8 characters")
                confirm_password = st.text_input("✅ Confirm Password", type="password", placeholder="Confirm your password")
                
                if st.form_submit_button("🌟 Create Account", use_container_width=True):
                    if password != confirm_password:
                        st.error("❌ Passwords don't match!")
                    elif name and email and password:
                        result = auth_manager.register_user(email, password, name)
                        if result['success']:
                            st.success("✅ Registration successful!")
                            st.session_state.registration_complete = True
                            st.rerun()
                        else:
                            st.error(result['error'])
            
            st.markdown("</div>", unsafe_allow_html=True)

# ============ MAIN APP ============
def show_main_app():
    """Display main application"""
    
    user = auth_manager.get_current_user()
    
    # Render header
    render_header()
    
    # ============ NAVIGATION WITH EQUAL SIZES ============
    st.markdown("""
    <div class="nav-container">
    """, unsafe_allow_html=True)
    
    nav_items = [
        ("🏠 Home", "Home"),
        ("📊 Assess", "Assessment"),
        ("🤖 AI Coach", "AI Advisor"),
        ("🎯 Missions", "Goals"),
        ("📈 Progress", "Dashboard"),
        ("🍽️ Food Saver", "Food"),
        ("🧠 ML Insights", "ML Insights")
    ]
    
    # Create columns for navigation
    cols = st.columns(7, gap="small")
    
    for idx, (col, (label, page)) in enumerate(zip(cols, nav_items)):
        with col:
            is_active = st.session_state.page == page
            # Add active class to button
            if is_active:
                st.markdown(f"""
                <button class="nav-btn-active" style="
                    background: linear-gradient(135deg, rgba(100, 200, 180, 0.25), rgba(74, 168, 160, 0.15));
                    border: 1px solid #64c8b4;
                    border-radius: 14px;
                    padding: 14px 8px;
                    color: #e8f0f0;
                    font-weight: 600;
                    font-size: 0.85rem;
                    min-height: 75px;
                    height: 75px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                    cursor: default;
                    width: 100%;
                    box-shadow: 0 5px 25px rgba(100, 200, 180, 0.15);
                    font-family: inherit;
                    background: linear-gradient(135deg, rgba(100, 200, 180, 0.25), rgba(74, 168, 160, 0.15));
                ">
                    {label}
                </button>
                """, unsafe_allow_html=True)
            else:
                if st.button(label, key=f"nav_{page}", use_container_width=True):
                    st.session_state.page = page
                    st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Page indicator
    st.markdown(f"""
    <div style="text-align: center; margin: 15px 0;">
        <span class="page-indicator">🌱 Currently Viewing: {st.session_state.page}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Page routing
    if st.session_state.page == "Home":
        show_home(user)
    elif st.session_state.page == "Assessment":
        show_assessment(user)
    elif st.session_state.page == "AI Advisor":
        show_ai_advisor(user)
    elif st.session_state.page == "Goals":
        show_goals(user)
    elif st.session_state.page == "Dashboard":
        show_dashboard(user)
    elif st.session_state.page == "Food":
        show_food_waste(user)
    elif st.session_state.page == "ML Insights":
        show_ml_insights(user)
    
    # Show results if flag is set
    if st.session_state.show_results and st.session_state.assessment_data:
        display_results(st.session_state.assessment_data, st.session_state.assessment_user)

# ============ HOME PAGE ============
def show_home(user):
    """Home dashboard with carbon theme"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>🌟 Welcome to Your Carbon Journey</h2>
        <p>Track your carbon footprint, earn achievements, and make a difference for our planet!</p>
        <div style="margin-top: 15px;">
            <span class="carbon-badge">🌱 Every Action Counts</span>
            <span class="carbon-badge" style="margin-left: 10px;">♻️ Reduce • Reuse • Recycle</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    stats = user.get('stats', {})
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.1s;">
            <div class="stat-icon">🌍</div>
            <div class="stat-number">{stats.get('total_assessments', 0)}</div>
            <div class="stat-label">Assessments Done</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.2s;">
            <div class="stat-icon">💚</div>
            <div class="stat-number">{stats.get('total_co2_saved', 0)}</div>
            <div class="stat-label">kg CO₂ Saved</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.3s;">
            <div class="stat-icon">🏆</div>
            <div class="stat-number">{stats.get('achievements_unlocked', 0)}</div>
            <div class="stat-label">Achievements</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.4s;">
            <div class="stat-icon">⭐</div>
            <div class="stat-number">{stats.get('level', 1)}</div>
            <div class="stat-label">Level</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Feature cards
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 48px;">📊</div>
            <h4>Carbon Assessment</h4>
            <p>Calculate your carbon footprint</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Take Assessment →", key="home_assess_btn", use_container_width=True):
            st.session_state.page = "Assessment"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 48px;">🤖</div>
            <h4>AI Recommendations</h4>
            <p>Get personalized sustainability tips</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Get AI Advice →", key="home_ai_btn", use_container_width=True):
            st.session_state.page = "AI Advisor"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size: 48px;">🎯</div>
            <h4>Eco Missions</h4>
            <p>Complete challenges and earn XP</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Missions →", key="home_missions_btn", use_container_width=True):
            st.session_state.page = "Goals"
            st.rerun()
    
    # Daily tip
    tips = [
        "💡 Turning off lights saves energy and money!",
        "🌿 Plant a tree to offset 21kg of CO₂ per year!",
        "🚶 Walking 1km instead of driving saves 0.21kg CO₂!",
        "🥗 Reducing meat consumption by 2 meals/week saves 8kg CO₂!",
        "♻️ Recycling 1kg of plastic saves 1.5kg CO₂!",
        "🚲 Biking instead of driving saves 2kg CO₂ per trip!",
        "💧 Fix leaky faucets to save water and energy!",
        "📦 Use reusable bags to reduce plastic waste!"
    ]
    
    st.markdown(f"""
    <div class="glass-card" style="margin-top: 25px;">
        <h3>💡 Daily Sustainability Tip</h3>
        <p style="font-size: 1.1rem; color: rgba(232, 240, 240, 0.9);">
            {random.choice(tips)}
        </p>
        <div style="margin-top: 15px; display: flex; gap: 10px; flex-wrap: wrap;">
            <span class="carbon-badge">🌱 Small Changes</span>
            <span class="carbon-badge">♻️ Big Impact</span>
            <span class="carbon-badge">🌍 Save the Planet</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============ ASSESSMENT ============
def show_assessment(user):
    """Carbon assessment"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>📊 Carbon Footprint Assessment</h2>
        <p>Answer a few questions and get instant results!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("assessment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🚗 Transportation")
            transport = st.selectbox(
                "Primary mode of transport",
                ["car", "public_transport", "bicycle", "walking", "electric_vehicle"]
            )
            
            distance = st.slider(
                "📏 Weekly distance (km)",
                min_value=0, max_value=500, value=100, step=10,
                format="%d km"
            )
            
            st.markdown("### ⚡ Home Energy")
            electricity = st.select_slider(
                "Energy usage level",
                options=["low", "medium", "high"],
                value="medium"
            )
        
        with col2:
            st.markdown("### 🥗 Dietary Choice")
            diet = st.selectbox(
                "Your diet preference",
                ["omnivore", "vegetarian", "vegan", "pescatarian"]
            )
            
            st.markdown("### 🛍️ Shopping Habits")
            shopping = st.select_slider(
                "Shopping frequency",
                options=["low", "medium", "high"],
                value="medium"
            )
            
            st.markdown("### 📍 Living Area")
            location = st.selectbox(
                "Where do you live?",
                ["Urban", "Suburban", "Rural"]
            )
        
        submitted = st.form_submit_button("🌱 Calculate My Impact", use_container_width=True)
        
        if submitted:
            with st.spinner("Calculating your carbon footprint..."):
                data = {
                    'transport_type': transport,
                    'weekly_distance': distance,
                    'electricity': electricity,
                    'diet': diet,
                    'shopping': shopping,
                    'location': location
                }
                
                footprint = calculator.calculate_footprint(data)
                
                # Save to database
                db.save_assessment(user['email'], {
                    'data': data,
                    'footprint': footprint,
                    'date': datetime.now().isoformat()
                })
                
                # Update user stats
                stats = user.get('stats', {})
                stats['total_assessments'] = stats.get('total_assessments', 0) + 1
                auth_manager.update_user_stats(user['email'], stats)
                
                st.balloons()
                st.success("🎉 Assessment complete! Check your results below!")
                
                # Store results in session state
                st.session_state.assessment_data = footprint
                st.session_state.assessment_user = user
                st.session_state.show_results = True
                st.rerun()

def display_results(footprint, user):
    """Display results with carbon theme"""
    
    st.markdown("## 📊 Your Carbon Snapshot")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card slide-up">
            <div class="stat-icon">🌫️</div>
            <div class="stat-number">{footprint['total']}</div>
            <div class="stat-label">kg CO₂/week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.1s;">
            <div class="stat-icon">💚</div>
            <div class="stat-number">{footprint['eco_score']}</div>
            <div class="stat-label">Eco Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        trees = int(footprint['total'] / 21)
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.2s;">
            <div class="stat-icon">🌳</div>
            <div class="stat-number">{trees}</div>
            <div class="stat-label">Trees/year</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        xp_earned = gamification.calculate_xp(footprint['eco_score'])
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.3s;">
            <div class="stat-icon">⭐</div>
            <div class="stat-number">+{xp_earned}</div>
            <div class="stat-label">XP Earned</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        categories = ['Transport', 'Food', 'Energy', 'Shopping']
        values = [footprint['transport'], footprint['food'], footprint['energy'], footprint['shopping']]
        
        fig = go.Figure(data=[
            go.Bar(
                x=categories, y=values,
                marker_color=['#ff6b6b', '#64c8b4', '#4aa8a0', '#45b7d1'],
                text=[f"{v} kg" for v in values],
                textposition='outside',
                textfont=dict(size=13, color='white'),
                marker_line_color='rgba(255,255,255,0.1)',
                marker_line_width=2
            )
        ])
        fig.update_layout(
            title=dict(text="<b>Category Breakdown</b>", font=dict(color='white'), x=0.5),
            plot_bgcolor='rgba(0,0,0,0.2)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            font=dict(color='white'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig2 = go.Figure(data=[go.Pie(
            labels=categories,
            values=values,
            hole=0.4,
            marker=dict(colors=['#ff6b6b', '#64c8b4', '#4aa8a0', '#45b7d1'], line=dict(color='rgba(255,255,255,0.1)', width=2)),
            textinfo='label+percent',
            textposition='outside',
            textfont=dict(size=13, color='white'),
            hoverinfo='label+value+percent'
        )])
        fig2.update_layout(
            title=dict(text="<b>Distribution</b>", font=dict(color='white'), x=0.5),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            font=dict(color='white'),
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Insight
    highest = max([('Transport', footprint['transport']), ('Food', footprint['food']), ('Energy', footprint['energy']), ('Shopping', footprint['shopping'])], key=lambda x: x[1])
    
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 20px; margin: 20px 0; border: 1px solid rgba(100,200,180,0.15);">
        <div style="display: flex; align-items: center; gap: 15px; flex-wrap: wrap;">
            <span style="font-size: 32px;">💡</span>
            <div>
                <strong style="color: #64c8b4; font-size: 1.05rem;">AI Insight:</strong>
                <span style="color: rgba(232, 240, 240, 0.9);">
                    Your biggest impact is from <strong style="color: #64c8b4;">{highest[0]}</strong> 
                    ({highest[1]} kg CO₂). Focus here for maximum reduction!
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🤖 Get AI Recommendations →", key="get_ai_recommendations_btn", use_container_width=True):
            st.session_state.page = "AI Advisor"
            st.session_state.show_results = False
            st.rerun()

# ============ AI ADVISOR ============
def show_ai_advisor(user):
    """AI recommendations"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>🤖 AI Sustainability Coach</h2>
        <p>Get personalized recommendations to reduce your carbon footprint!</p>
    </div>
    """, unsafe_allow_html=True)
    
    assessments = db.get_assessments(user['email'])
    
    if not assessments:
        st.warning("⚠️ Complete an assessment first to get recommendations!")
        if st.button("Take Assessment Now", key="take_assessment_now_btn"):
            st.session_state.page = "Assessment"
            st.rerun()
        return
    
    latest = assessments[-1]
    footprint = latest['footprint']
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Generate AI Recommendations", key="generate_ai_recs_btn", use_container_width=True):
            with st.spinner("🤖 AI is analyzing your lifestyle..."):
                if ai_advisor:
                    recs = ai_advisor.generate_recommendations(
                        latest['data'],
                        footprint
                    )
                else:
                    recs = [
                        {"action": "Switch to public transport 2 days/week", "co2_reduction": "8.4 kg/week", "difficulty": "Easy", "savings": "$15/week"},
                        {"action": "Reduce meat consumption to 3 days/week", "co2_reduction": "12 kg/week", "difficulty": "Medium", "savings": "$20/week"},
                        {"action": "Switch to LED bulbs everywhere", "co2_reduction": "3.5 kg/week", "difficulty": "Easy", "savings": "$8/week"}
                    ]
                
                st.session_state.recommendations = recs
    
    if st.session_state.recommendations:
        st.markdown("### 🎯 Your Custom Action Plan")
        
        for idx, rec in enumerate(st.session_state.recommendations, 1):
            diff_colors = {"Easy": "#64c8b4", "Medium": "#ffd93d", "Hard": "#ff6b6b"}
            color = diff_colors.get(rec.get('difficulty', 'Medium'), '#64c8b4')
            
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 20px; margin: 15px 0; border-left: 4px solid {color};">
                <h3 style="color: #e8f0f0; margin: 0 0 10px 0;">{idx}. {rec['action']}</h3>
                <div style="display: flex; gap: 20px; flex-wrap: wrap; color: rgba(232, 240, 240, 0.8);">
                    <span style="background: rgba(255,255,255,0.05); padding: 5px 12px; border-radius: 20px;">
                        📉 Impact: {rec.get('co2_reduction', 'N/A')}
                    </span>
                    <span style="background: rgba(255,255,255,0.05); padding: 5px 12px; border-radius: 20px; color: {color};">
                        🎯 Difficulty: {rec.get('difficulty', 'Medium')}
                    </span>
                    <span style="background: rgba(255,255,255,0.05); padding: 5px 12px; border-radius: 20px;">
                        💰 Savings: {rec.get('savings', 'N/A')}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ============ GOALS ============
def show_goals(user):
    """Goals and missions"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>🎯 Weekly Eco Missions</h2>
        <p>Complete missions to earn XP and achievements!</p>
    </div>
    """, unsafe_allow_html=True)
    
    goal_manager = GoalManager()
    goals = goal_manager.get_weekly_goals()
    progress = goal_manager.get_progress()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card slide-up">
            <div class="stat-number">{progress['completed']}/{progress['total']}</div>
            <div class="stat-label">✅ Goals Done</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.1s;">
            <div class="stat-number">{progress['total_xp']}</div>
            <div class="stat-label">⭐ XP Earned</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.2s;">
            <div class="stat-number">{progress['percentage']:.0f}%</div>
            <div class="stat-label">📊 Progress</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.progress(progress['percentage'] / 100)
    st.markdown("<br>", unsafe_allow_html=True)
    
    for goal in goals:
        col1, col2, col3, col4, col5 = st.columns([3, 2, 1, 1, 1])
        
        with col1:
            st.markdown(f"**{goal['title']}**")
            st.caption(goal['description'])
        with col2:
            st.markdown(f"🌱 Saves: {goal['co2_saved']}")
        with col3:
            st.markdown(f"⭐ +{goal['xp']} XP")
        with col4:
            st.markdown(f"📊 {goal['difficulty']}")
        with col5:
            if not goal['completed']:
                if st.button(f"✅ Complete", key=f"complete_goal_{goal['id']}"):
                    goal_manager.complete_goal(goal['id'])
                    stats = user.get('stats', {})
                    stats['xp'] = stats.get('xp', 0) + goal['xp']
                    auth_manager.update_user_stats(user['email'], stats)
                    st.balloons()
                    st.success(f"🎉 You earned {goal['xp']} XP!")
                    st.rerun()
            else:
                st.markdown("✅ **Done!**")
        st.markdown("---")

# ============ DASHBOARD ============
def show_dashboard(user):
    """Progress dashboard"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>📈 Your Progress Dashboard</h2>
        <p>Track your sustainability journey over time!</p>
    </div>
    """, unsafe_allow_html=True)
    
    assessments = db.get_assessments(user['email'])
    
    if not assessments:
        st.info("💡 Complete your first assessment to see your dashboard!")
        if st.button("Take Assessment", key="dashboard_take_assessment"):
            st.session_state.page = "Assessment"
            st.rerun()
        return
    
    # Extract data
    dates = []
    scores = []
    totals = []
    
    for ass in assessments[-10:]:
        dates.append(datetime.fromisoformat(ass['date']).strftime('%d %b'))
        scores.append(ass['footprint']['eco_score'])
        totals.append(ass['footprint']['total'])
    
    # Trend chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=totals,
        mode='lines+markers',
        name='CO₂ Emissions',
        line=dict(color='#ff6b6b', width=3),
        marker=dict(size=10, color='#ff6b6b'),
        fill='tozeroy',
        fillcolor='rgba(255,107,107,0.1)'
    ))
    fig.add_trace(go.Scatter(
        x=dates, y=scores,
        mode='lines+markers',
        name='Eco Score',
        line=dict(color='#64c8b4', width=3),
        marker=dict(size=10, color='#64c8b4'),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title=dict(text="<b>Your Progress Over Time</b>", font=dict(color='white'), x=0.5),
        plot_bgcolor='rgba(0,0,0,0.2)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
        font=dict(color='white'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(title="kg CO₂/week", titlefont=dict(color='white'), gridcolor='rgba(255,255,255,0.05)'),
        yaxis2=dict(title="Eco Score", titlefont=dict(color='white'), overlaying='y', side='right', gridcolor='rgba(255,255,255,0.05)'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============ FOOD WASTE ============
def show_food_waste(user):
    """Food waste helper"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>🍽️ Smart Food Waste Assistant</h2>
        <p>Enter ingredients, get recipes, and reduce food waste!</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'food_items' not in st.session_state:
        st.session_state.food_items = []
    
    col1, col2 = st.columns([3, 1])
    with col1:
        new_item = st.text_input("Add ingredient", placeholder="e.g., tomatoes, chicken, rice")
    with col2:
        if st.button("➕ Add", key="add_food_item_btn", use_container_width=True):
            if new_item and new_item.strip():
                st.session_state.food_items.append(new_item.strip())
                st.rerun()
    
    if st.session_state.food_items:
        st.markdown("### 📦 Your Ingredients")
        
        cols = st.columns(5)
        for idx, item in enumerate(st.session_state.food_items):
            with cols[idx % 5]:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); border-radius: 15px; padding: 12px; text-align: center; border: 1px solid rgba(255,255,255,0.06);">
                    <div style="font-size: 24px;">📦</div>
                    <div style="color: #e8f0f0; font-weight: 600; font-size: 0.9rem;">{item}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("❌", key=f"remove_food_{idx}"):
                    st.session_state.food_items.pop(idx)
                    st.rerun()
        
        if st.button("🌱 Get Smart Suggestions", key="get_smart_suggestions_btn", use_container_width=True, type="primary"):
            with st.spinner("Generating suggestions..."):
                recipes = [
                    "🍳 Create a delicious stir-fry with your ingredients!",
                    "🥗 Make a fresh salad or wrap!",
                    "🍜 Turn it into a hearty soup!"
                ]
                
                tips = [
                    "📦 Store vegetables in produce drawers to keep them fresh longer",
                    "🧊 Freeze items before they spoil",
                    "♻️ Use vegetable scraps for making broth"
                ]
                
                st.markdown("### 💡 Smart Suggestions")
                
                for recipe in recipes:
                    st.success(recipe)
                for tip in tips:
                    st.info(tip)
                
                stats = user.get('stats', {})
                stats['xp'] = stats.get('xp', 0) + 10
                auth_manager.update_user_stats(user['email'], stats)
                st.success("⭐ +10 XP for reducing food waste!")
    
    else:
        st.info("✨ Add some ingredients above to get personalized suggestions!")

# ============ ML INSIGHTS ============
def show_ml_insights(user):
    """ML-powered insights dashboard"""
    
    st.markdown("""
    <div class="glass-card slide-up">
        <h2>🧠 AI & ML Insights</h2>
        <p>Powered by Machine Learning for smarter sustainability decisions</p>
        <div style="margin-top: 10px; display: flex; gap: 10px; flex-wrap: wrap;">
            <span class="carbon-badge">🤖 Advanced Analytics</span>
            <span class="carbon-badge">📊 Predictive Modeling</span>
            <span class="carbon-badge">🎯 Personalization</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    assessments = db.get_assessments(user['email'])
    
    if not assessments:
        st.warning("⚠️ Complete some assessments to unlock ML insights!")
        if st.button("Take Assessment Now", key="ml_take_assessment"):
            st.session_state.page = "Assessment"
            st.rerun()
        return
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Check if ML models are trained
    model_path = "data/ml_models/carbon_predictor.pkl"
    models_trained = os.path.exists(model_path)
    
    if not models_trained:
        st.warning("⚠️ ML Models not trained yet!")
        st.info("💡 Please run the following command in your terminal:\n```\npython train_ml.py\n```")
        if st.button("🔄 Check Again", key="check_models_btn"):
            st.rerun()
        return
    
    # Get latest assessment data
    latest = assessments[-1]
    user_data = latest['data']
    footprint = latest['footprint']
    
    # Row 1: Overview Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card slide-up">
            <div class="stat-icon">📊</div>
            <div class="stat-number">{len(assessments)}</div>
            <div class="stat-label">Total Assessments</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.1s;">
            <div class="stat-icon">📈</div>
            <div class="stat-number">{footprint['eco_score']}</div>
            <div class="stat-label">Current Eco Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        try:
            cluster = user_clustering.predict_cluster(user_data)
            cluster_name = user_clustering.get_cluster_profile(cluster) if cluster is not None else "🔍 Analyzing..."
        except:
            cluster_name = "🔄 Loading..."
        
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.2s;">
            <div class="stat-icon">🧑‍🤝‍🧑</div>
            <div class="stat-number" style="font-size: 1.1rem;">{cluster_name[:30]}</div>
            <div class="stat-label">User Profile</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        try:
            prediction = carbon_predictor.predict_footprint(user_data, assessments)
        except:
            prediction = footprint['total']
        
        st.markdown(f"""
        <div class="stat-card slide-up" style="animation-delay: 0.3s;">
            <div class="stat-icon">🔮</div>
            <div class="stat-number">{prediction}</div>
            <div class="stat-label">Predicted Footprint (kg)</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Row 2: Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📉 Future Trend Prediction")
        
        if len(assessments) >= 3:
            try:
                future = carbon_predictor.predict_future_trend(assessments, weeks=4)
                
                if future:
                    historical_emissions = [d['footprint']['total'] for d in assessments[-5:]]
                    historical_weeks = [f"Past {i+1}" for i in range(len(historical_emissions))]
                    future_weeks = [f"Week {i+1}" for i in range(future['weeks'])]
                    future_values = future['predictions']
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=historical_weeks, y=historical_emissions,
                        mode='lines+markers', name='Historical',
                        line=dict(color='#ff6b6b', width=3),
                        marker=dict(size=8, color='#ff6b6b')
                    ))
                    fig.add_trace(go.Scatter(
                        x=future_weeks, y=future_values,
                        mode='lines+markers', name='Predicted',
                        line=dict(color='#64c8b4', width=3, dash='dash'),
                        marker=dict(size=8, color='#64c8b4')
                    ))
                    fig.update_layout(
                        title=dict(text="<b>Carbon Trend Forecast</b>", font=dict(color='white'), x=0.5),
                        plot_bgcolor='rgba(0,0,0,0.2)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        height=350,
                        font=dict(color='white'),
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
                        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
                        yaxis=dict(gridcolor='rgba(255,255,255,0.05)', title="kg CO₂/week")
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    trend = future['current_trend']
                    if trend < 0:
                        st.success(f"📉 **Positive Trend!** Emissions decreasing by {abs(trend):.2f} kg CO₂/week")
                    elif trend > 0:
                        st.warning(f"📈 **Alert!** Emissions increasing by {trend:.2f} kg CO₂/week")
                    else:
                        st.info("📊 **Stable!** Emissions are consistent")
            except:
                st.info("💡 Need more data for trend prediction")
        else:
            st.info("💡 Complete at least 3 assessments for trend analysis!")
    
    with col2:
        st.markdown("### 🎯 ML-Powered Recommendations")
        
        if st.button("🚀 Generate ML Recommendations", key="ml_generate_btn", use_container_width=True):
            with st.spinner("🧠 AI is analyzing patterns..."):
                try:
                    recs = recommendation_engine.get_personalized_recommendations(
                        user_data,
                        footprint,
                        assessments
                    )
                    if recs:
                        st.session_state.ml_recommendations = recs
                except Exception as e:
                    st.warning(f"⚠️ Could not generate recommendations: {str(e)}")
        
        if st.session_state.ml_recommendations:
            for idx, rec in enumerate(st.session_state.ml_recommendations, 1):
                diff_colors = {"Easy": "#64c8b4", "Medium": "#ffd93d", "Hard": "#ff6b6b"}
                color = diff_colors.get(rec.get('difficulty', 'Medium'), '#64c8b4')
                confidence = rec.get('confidence', 85)
                
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.04); border-radius: 16px; padding: 15px; margin: 10px 0; border-left: 4px solid {color};">
                    <h4 style="color: #e8f0f0; margin: 0 0 8px 0;">{idx}. {rec['action']}</h4>
                    <div style="display: flex; gap: 15px; flex-wrap: wrap; color: rgba(232,240,240,0.7); font-size: 0.9rem;">
                        <span>📉 {rec['co2_reduction']}</span>
                        <span>🎯 {rec['difficulty']}</span>
                        <span>💰 {rec['savings']}</span>
                        <span>🎯 Match: {confidence}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("👆 Click the button above to get AI-powered recommendations")

# ============ MAIN ============
if __name__ == "__main__":
    if not auth_manager.is_logged_in():
        show_auth_page()
    else:
        show_main_app()