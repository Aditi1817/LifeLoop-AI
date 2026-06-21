"""
Reusable UI components for LifeLoop AI
"""

import streamlit as st
from .styles import PREMIUM_CSS, AUTH_CSS

def render_premium_css():
    """Render premium CSS styles"""
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

def render_auth_css():
    """Render authentication CSS styles"""
    st.markdown(AUTH_CSS, unsafe_allow_html=True)

def render_stat_card(icon: str, value: str, label: str, delay: float = 0, color: str = "white"):
    """Render a stat card with animation"""
    st.markdown(f"""
    <div class="stat-card" style="animation-delay: {delay}s; border-color: {color}33;">
        <div style="font-size: 36px;">{icon}</div>
        <div class="stat-number">{value}</div>
        <div class="stat-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def render_glass_card(content: str, title: str = "", height: str = "auto"):
    """Render a glass card"""
    title_html = f'<h2 style="color: white; margin-bottom: 15px;">{title}</h2>' if title else ''
    st.markdown(f"""
    <div class="glass-card" style="height: {height};">
        {title_html}
        {content}
    </div>
    """, unsafe_allow_html=True)

def render_toast(message: str, type: str = "success", duration: int = 3):
    """Render a toast notification"""
    colors = {
        "success": "#4CAF50",
        "error": "#f44336",
        "info": "#2196F3",
        "warning": "#ff9800"
    }
    
    st.markdown(f"""
    <div class="toast" style="border-left: 4px solid {colors.get(type, '#4CAF50')};">
        {message}
    </div>
    """, unsafe_allow_html=True)

def render_feature_card(icon: str, title: str, description: str):
    """Render a feature card"""
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px);
                border-radius: 16px; padding: 20px; text-align: center;
                border: 1px solid rgba(255,255,255,0.1);
                transition: all 0.3s ease;">
        <div style="font-size: 48px; margin-bottom: 15px;">{icon}</div>
        <h3 style="color: white; margin-bottom: 10px;">{title}</h3>
        <p style="color: rgba(255,255,255,0.8);">{description}</p>
    </div>
    """, unsafe_allow_html=True)

def render_loading_spinner(message: str = "Loading..."):
    """Render a loading spinner"""
    st.markdown(f"""
    <div style="text-align: center; padding: 40px;">
        <div style="display: inline-block; width: 50px; height: 50px;
                    border: 5px solid rgba(255,255,255,0.1);
                    border-top: 5px solid #FFE66D;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;"></div>
        <p style="color: white; margin-top: 20px;">{message}</p>
    </div>
    <style>
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
    """, unsafe_allow_html=True)

def render_divider():
    """Render a styled divider"""
    st.markdown("""
    <hr style="border: none; height: 2px; 
               background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
               margin: 30px 0;">
    """, unsafe_allow_html=True)

def render_progress_bar(value: float, label: str = "", color: str = "#FFE66D"):
    """Render a custom progress bar"""
    st.markdown(f"""
    <div style="margin: 10px 0;">
        {f'<div style="color: white; margin-bottom: 5px;">{label}</div>' if label else ''}
        <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 10px; overflow: hidden;">
            <div style="width: {value}%; height: 100%; background: {color}; border-radius: 10px;
                        transition: width 0.5s ease;">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)