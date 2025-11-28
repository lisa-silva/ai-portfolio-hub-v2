import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Lisa Silva - AI Portfolio Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #FF4B4B, #FF8C42);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .app-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    .app-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    .category-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #FF4B4B;
        padding-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-header">Lisa Silva</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Engineer | 21+ Production Applications | Full-Stack Deployment</div>', unsafe_allow_html=True)

# Stats Overview
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="stats-card">
        <h3>21+</h3>
        <p>Production Apps</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <h3>99.1%</h3>
        <p>AI Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <h3>2 Months</h3>
        <p>Acceleration</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-card">
        <h3>100%</h3>
        <p>Deployed Live</p>
    </div>
    """, unsafe_allow_html=True)

# Introduction
st.markdown("""
### 🎯 Production-Ready Application Portfolio

Welcome to my centralized portfolio hub showcasing **21+ deployed Streamlit applications**. Every application below is live, functional, and demonstrates real-world problem-solving capabilities. This portfolio represents intensive development and rapid deployment over the past months.
""")

# Applications Data
apps_data = [
    # Business & Compliance Suite
    {
        "name": "ARCHON Detector",
        "category": "Business & Compliance Suite",
        "description": "Compliance AI with 99.1% accuracy in regulatory analysis",
        "url": "https://archon-detector-app-lisa-silva.streamlit.app/",
        "emoji": "🛡️",
        "status": "Production"
    },
    {
        "name": "AUDITUS XAI",
        "category": "Business & Compliance Suite", 
        "description": "Explainable AI for compliance detection and reasoning transparency",
        "url": "https://auditus-xai-lisa-silva.streamlit.app/",
        "emoji": "🔍",
        "status": "Production"
    },
    {
        "name": "RegTech Suite",
        "category": "Business & Compliance Suite",
        "description": "Comprehensive regulatory technology applications",
        "url": "https://comply-rag-lisa-silva.streamlit.app/",
        "emoji": "⚖️",
        "status": "Production"
    },
    {
        "name": "LeaseSync AI",
        "category": "Business & Compliance Suite",
        "description": "Real estate and lease management automation",
        "url": "https://lease-sync-ai-lisa-silva.streamlit.app/",
        "emoji": "🏢",
        "status": "Production"
    },
    {
        "name": "Finance Tracker",
        "category": "Business & Compliance Suite", 
        "description": "Personal finance management and analysis",
        "url": "https://finance-tracker-app-lisa-silva.streamlit.app/",
        "emoji": "💰",
        "status": "Production"
    },
    {
        "name": "CSV Data Analyzer",
        "category": "Business & Compliance Suite",
        "description": "Business data analysis and visualization tool",
        "url": "https://csv-data-analyzer-lisa-silva.streamlit.app/",
        "emoji": "📊",
        "status": "Production"
    },
    {
        "name": "Cherrywood Nuisance Reporter",
        "category": "Business & Compliance Suite",
        "description": "Apartment community reporting tool for noise and issues",
        "url": "https://cherrywood-nuisance-reporter-dashboard.streamlit.app/",
        "emoji": "🏘️",
        "status": "Production"
    },
    
    # Productivity & Tools
    {
        "name": "Plumber Portal",
        "category": "Productivity & Tools",
        "description": "White-label service request system for businesses",
        "url": "https://plumber-service-request-app-lisa-silva.streamlit.app/",
        "emoji": "🔧",
        "status": "Production"
    },
    {
        "name": "Structured Meal Planner", 
        "category": "Productivity & Tools",
        "description": "AI-powered nutrition planning and meal organization",
        "url": "https://structured-ai-meal-planner-lisa-silva.streamlit.app/",
        "emoji": "🍽️",
        "status": "Production"
    },
    {
        "name": "Web Scraper",
        "category": "Productivity & Tools",
        "description": "Data extraction and analysis from web sources",
        "url": "https://web-scraper-lisa-silva.streamlit.app/",
        "emoji": "🕷️",
        "status": "Production"
    },
    
    # AI & Research Applications
    {
        "name": "Premise Challenger",
        "category": "AI & Research Applications",
        "description": "Argument analysis and critical thinking enhancement",
        "url": "https://premisechallengerapp-6hddzjrxz2v6fqntajsaw8.streamlit.app/",
        "emoji": "💭",
        "status": "Production"
    },
    {
        "name": "Political Fact Checker",
        "category": "AI & Research Applications",
        "description": "Information verification and analysis system", 
        "url": "https://political-fact-checker-lisa-silva-v2.streamlit.app/",
        "emoji": "🇺🇸",
        "status": "Production"
    },
    {
        "name": "Dark Triad Analyzer",
        "category": "AI & Research Applications",
        "description": "Psychological assessment and personality analysis",
        "url": "https://dark-triad-detector-quiz-lisa-silva-v2.streamlit.app/",
        "emoji": "🧠",
        "status": "Production"
    },
    {
        "name": "Catechism Scripture Analyzer",
        "category": "AI & Research Applications", 
        "description": "Religious text analysis and exploration",
        "url": "https://catechism-scripture-analyzer-lisa-silva.streamlit.app/",
        "emoji": "📖",
        "status": "Production"
    },
    {
        "name": "Review Sentiment Analyzer",
        "category": "AI & Research Applications",
        "description": "Customer feedback analysis and sentiment detection",
        "url": "https://online-review-sentiment-analyzer-lisa-silva.streamlit.app/",
        "emoji": "⭐",
        "status": "Production"
    },
    {
        "name": "Quantum Me App",
        "category": "AI & Research Applications",
        "description": "Personal development and goal tracking system",
        "url": "https://quantum-me-lisa-silva.streamlit.app/",
        "emoji": "🎯",
        "status": "Production"
    },
    
    # Portfolio & Demonstration
    {
        "name": "AI Portfolio Hub",
        "category": "Portfolio & Demonstration", 
        "description": "Centralized showcase of all applications (this app)",
        "url": "https://ai-portfolio-apps-lisa-silva.streamlit.app/",
        "emoji": "🎪",
        "status": "Production"
    },
    {
        "name": "FlagPro Shift Scheduling",
        "category": "Portfolio & Demonstration",
        "description": "Workforce management system simulation",
        "url": "https://flagpro-shift-scheduling-lisa-silva.streamlit.app/",
        "emoji": "🚩",
        "status": "Production"
    },
    
    # Innovative Tools
    {
        "name": "Voidism",
        "category": "Innovative Tools",
        "description": "Scream into the void instead of texting your ex - nothing is ever sent",
        "url": "https://voidism.streamlit.app/",
        "emoji": "🕳️",
        "status": "Production"
    },
    {
        "name": "Anti-Ex Text Generator", 
        "category": "Innovative Tools",
        "description": "Generates perfect responses when toxic exes break no-contact",
        "url": "https://anti-ex-text-generator.streamlit.app/",
        "emoji": "🚫",
        "status": "Production"
    },
    {
        "name": "Void Text",
        "category": "Innovative Tools",
        "description": "Fake texting app for rage-texting without sending anything",
        "url": "https://void-text-stay-no-contact.streamlit.app/",
        "emoji": "📱",
        "status": "Production"
    }
]
categories = ["Business & Compliance Suite", "Productivity & Tools", "AI & Research Applications", "Portfolio & Demonstration", "Innovative Tools"]

# Display apps by category

for category in categories:
    st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)
    
    category_apps = [app for app in apps_data if app["category"] == category]
    
    for app in category_apps:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="app-card">
                <h4>{app['emoji']} {app['name']}</h4>
                <p>{app['description']}</p>
                <small><strong>Status:</strong> {app['status']}</small>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <br><br>
            <a href="{app['url']}" target="_blank">
                <button style="
                    background: linear-gradient(45deg, #FF4B4B, #FF8C42);
                    color: white;
                    border: none;
                    padding: 0.5rem 1rem;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold;
                    width: 100%;
                ">Launch App</button>
            </a>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
### 🚀 Technical Stack & Deployment
- **Framework:** Streamlit
- **Language:** Python
- **Deployment:** Streamlit Cloud
- **Version Control:** GitHub
- **Infrastructure:** Google Cloud Platform

### 📬 Connect With Me
- **LinkedIn:** [Lisa Silva](https://www.linkedin.com/in/lisa-silva-706649391/)
- **GitHub:** [lisa-silva](https://github.com/lisa-silva)

*All applications are production-ready and publicly accessible. Last updated: {date}*
""".format(date=datetime.now().strftime("%B %d, %Y")))

# Sidebar for quick stats
with st.sidebar:
    st.markdown("### 📊 Portfolio Stats")
    st.metric("Total Applications", "21")
    st.metric("Categories", "5")
    st.metric("Deployment Rate", "100%")
    st.metric("Top Accuracy", "99.1%")
    
    st.markdown("### 🔍 Quick Search")
    search_term = st.text_input("Find an application...")
    if search_term:
        filtered_apps = [app for app in apps_data if search_term.lower() in app['name'].lower() or search_term.lower() in app['description'].lower()]
        for app in filtered_apps:
            st.write(f"**{app['emoji']} {app['name']}**")
            st.caption(app['description'])
            st.markdown(f"[Launch App]({app['url']})")
