"""
Animation helpers for LifeLoop AI
"""

import streamlit as st
import time

class Animations:
    """Animation utilities"""
    
    @staticmethod
    def fade_in(element, duration: float = 0.5):
        """Create fade-in effect"""
        st.markdown(f"""
        <style>
            @keyframes fadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            .fade-in {{
                animation: fadeIn {duration}s ease-out;
            }}
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def slide_up(element, duration: float = 0.5):
        """Create slide-up effect"""
        st.markdown(f"""
        <style>
            @keyframes slideUp {{
                from {{ opacity: 0; transform: translateY(30px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            .slide-up {{
                animation: slideUp {duration}s ease-out;
            }}
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def pulse(element, duration: float = 2.0):
        """Create pulse effect"""
        st.markdown(f"""
        <style>
            @keyframes pulse {{
                0%, 100% {{ transform: scale(1); }}
                50% {{ transform: scale(1.05); }}
            }}
            .pulse {{
                animation: pulse {duration}s ease-in-out infinite;
            }}
        </style>
        """, unsafe_allow_html=True)