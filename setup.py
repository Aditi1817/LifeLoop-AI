"""
Setup script for LifeLoop AI
"""

from setuptools import setup, find_packages

setup(
    name="lifeloop-ai",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.29.0",
        "google-generativeai>=0.3.0",
        "plotly>=5.18.0",
        "pandas>=2.1.0",
        "python-dotenv>=1.0.0",
        "bcrypt>=4.1.0",
        "pyjwt>=2.8.0",
    ],
    entry_points={
        "console_scripts": [
            "lifeloop=app:main",
        ],
    },
)