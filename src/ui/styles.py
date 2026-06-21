"""
Custom CSS styles for LifeLoop AI
"""

PREMIUM_CSS = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:400,500,600,700,800,900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Hide default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Glass morphism cards */
    .glass-card {
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 30px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        color: white;
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 30px 80px rgba(0,0,0,0.4);
    }
    
    .glass-card h1, .glass-card h2, .glass-card h3 {
        color: white !important;
    }
    
    .glass-card p {
        color: rgba(255,255,255,0.9) !important;
    }
    
    /* Premium buttons */
    .stButton > button {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 12px 30px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 5px 20px rgba(255,107,107,0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 30px rgba(255,107,107,0.6);
        background: linear-gradient(135deg, #FF8E53, #FF6B6B);
    }
    
    /* Stat cards */
    .stat-card {
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        animation: slideUp 0.6s ease-out forwards;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: scale(1.05);
        background: rgba(255,255,255,0.25);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 900;
        color: #FFE66D;
        text-shadow: 0 0 30px rgba(255,230,109,0.3);
    }
    
    .stat-label {
        color: rgba(255,255,255,0.9);
        font-weight: 500;
        margin-top: 5px;
    }
    
    /* Animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .float-animation {
        animation: float 3s ease-in-out infinite;
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    .toast {
        animation: slideInRight 0.5s ease-out;
        padding: 15px 25px;
        border-radius: 15px;
        background: rgba(0,0,0,0.8);
        color: white;
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
    }
    
    /* Auth container */
    .auth-container {
        max-width: 450px;
        margin: 0 auto;
        padding: 40px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #FF8E53, #FF6B6B);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .stat-number { font-size: 2rem; }
        .glass-card { padding: 20px; }
        .auth-container { padding: 25px; margin: 10px; }
        .stButton > button { padding: 10px 20px; font-size: 0.9rem; }
    }
</style>
"""

AUTH_CSS = """
<style>
    .auth-container {
        max-width: 450px;
        margin: 0 auto;
        padding: 40px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .auth-container input {
        background: rgba(255,255,255,0.9);
        border-radius: 12px;
        padding: 12px 18px;
        border: none;
        width: 100%;
        font-size: 1rem;
        color: #2c3e50;
        margin-bottom: 15px;
    }
    
    .auth-container input:focus {
        outline: 2px solid #FF6B6B;
        box-shadow: 0 0 20px rgba(255,107,107,0.2);
    }
    
    .auth-container .stButton > button {
        width: 100%;
        padding: 14px;
        font-size: 1.1rem;
    }
    
    .auth-title {
        text-align: center;
        color: white;
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 10px;
    }
    
    .auth-subtitle {
        text-align: center;
        color: rgba(255,255,255,0.8);
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    
    .auth-logo {
        text-align: center;
        font-size: 80px;
        animation: float 3s ease-in-out infinite;
        margin-bottom: 20px;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
</style>
"""