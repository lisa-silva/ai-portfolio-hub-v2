import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Lisa Silva - AI Portfolio Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3.5rem; font-weight: 700; background: linear-gradient(45deg, #FF4B4B, #FF8C42);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin-bottom: 0.5rem;}
    .subtitle {font-size: 1.5rem; color: #666; text-align: center; margin-bottom: 2rem;}
    .app-card {background: white; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #FF4B4B;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 1rem; transition: transform 0.2s;}
    .app-card:hover {transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.15);}
    .stats-card {background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1.5rem;
        border-radius: 10px; text-align: center;}
    .category-header {font-size: 1.8rem; font-weight: 600; color: #333; margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #FF4B4B; padding-bottom: 0.5rem;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">Lisa Silva</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Engineer | 21+ Production Applications | Full-Stack Deployment</div>', unsafe_allow_html=True)

# Stats
c1, c2, c3, c4 = st.columns(4)
for col, num, label in zip([c1,c2,c3,c4], ["21+", "99.1%", "2 Months", "100%"], ["Production Apps", "AI Accuracy", "Acceleration", "Deployed Live"]):
    with col:
        st.markdown(f'<div class="stats-card"><h3>{num}</h3><p>{label}</p></div>', unsafe_allow_html=True)

st.markdown("### Production-Ready AI Application Portfolio")
st.markdown("Central hub for **21+ live, production-grade AI applications** — all built and deployed by Lisa Silva.")

# FIXED: All emojis are real Unicode — no more "Target", "Triangular Flag", etc.
apps_data = [
    # Business & Compliance Suite
    {"name": "ARCHON Detector", "category": "Business & Compliance Suite", "description": "Regulatory compliance AI with 99.1% accuracy", "url": "https://archon-detector-app-lisa-silva.streamlit.app/", "emoji": "🛡️"},
    {"name": "AUDITUS XAI", "category": "Business & Compliance Suite", "description": "Explainable AI for compliance reasoning", "url": "https://auditus-xai-lisa-silva.streamlit.app/", "emoji": "🔍"},
    {"name": "RegTech Suite", "category": "Business & Compliance Suite", "description": "Comprehensive regulatory technology platform", "url": "https://comply-rag-lisa-silva.streamlit.app/", "emoji": "⚖️"},
    {"name": "LeaseSync AI", "category": "Business & Compliance Suite", "description": "Automated lease management system", "url": "https://lease-sync-ai-lisa-silva.streamlit.app/", "emoji": "🏢"},
    {"name": "Finance Tracker", "category": "Business & Compliance Suite", "description": "Personal finance analysis tool", "url": "https://finance-tracker-app-lisa-silva.streamlit.app/", "emoji": "💰"},
    {"name": "CSV Data Analyzer", "category": "Business & Compliance Suite", "description": "Business data visualization platform", "url": "https://csv-data-analyzer-lisa-silva.streamlit.app/", "emoji": "📊"},
    {"name": "Cherrywood Nuisance Reporter", "category": "Business & Compliance Suite", "description": "Community issue reporting dashboard", "url": "https://cherrywood-nuisance-reporter-dashboard.streamlit.app/", "emoji": "🏘️"},

    # Productivity & Tools
    {"name": "FixSync", "category": "Productivity & Tools", "description": "Live visual repair collaboration — any trade", "url": "https://fixsync-lisa-silva.streamlit.app/", "emoji": "🔧"},
    {"name": "PlumbGuard", "category": "Productivity & Tools", "description": "AI plumbing portal — photos → live quotes", "url": "https://plumbguard-lisa-silva-app.streamlit.app/", "emoji": "🔧"},
    {"name": "Universal Business VMS", "category": "Productivity & Tools", "description": "Universal service + asset tracking platform", "url": "https://universal-business-vms-platform.streamlit.app/", "emoji": "🏭"},

    # AI & Research
    {"name": "Political Fact Checker", "category": "AI & Research Applications", "description": "Real-time political claim verification", "url": "https://political-fact-checker-lisa-silva-v2.streamlit.app/", "emoji": "🇺🇸"},
    {"name": "Dark Triad Analyzer", "category": "AI & Research Applications", "description": "Psychological trait assessment", "url": "https://dark-triad-detector-quiz-lisa-silva-v2.streamlit.app/", "emoji": "🧠"},
    {"name": "Catechism Scripture Analyzer", "category": "AI & Research Applications", "description": "Religious text exploration tool", "url": "https://catechism-scripture-analyzer-lisa-silva.streamlit.app/", "emoji": "📖"},
    {"name": "Review Sentiment Analyzer", "category": "AI & Research Applications", "description": "Customer feedback sentiment detection", "url": "https://online-review-sentiment-analyzer-lisa-silva.streamlit.app/", "emoji": "⭐"},
    {"name": "Quantum Me App", "category": "AI & Research Applications", "description": "Personal growth & goal tracking system", "url": "https://quantum-me-lisa-silva.streamlit.app/", "emoji": "🎯"},

    # Demo & Innovative
    {"name": "FlagPro Shift Scheduling", "category": "Portfolio & Demonstration", "description": "Workforce scheduling simulator", "url": "https://flagpro-shift-scheduling-lisa-silva.streamlit.app/", "emoji": "🚩"},
    {"name": "Voidism", "category": "Innovative Tools", "description": "Scream into the void — never sent", "url": "https://voidism.streamlit.app/", "emoji": "🕳️"},
    {"name": "Anti-Ex Text Generator", "category": "Innovative Tools", "description": "Perfect no-contact replies", "url": "https://anti-ex-text-generator.streamlit.app/", "emoji": "🚫"},
    {"name": "Void Text", "category": "Innovative Tools", "description": "Rage-text without sending", "url": "https://void-text-stay-no-contact.streamlit.app/", "emoji": "📱"},
]

categories = ["Business & Compliance Suite", "Productivity & Tools", "AI & Research Applications", "Portfolio & Demonstration", "Innovative Tools"]

# Display apps
for category in categories:
    st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)
    for app in [a for a in apps_data if a["category"] == category]:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(f'''
            <div class="app-card">
                <h4>{app["emoji"]} {app["name"]}</h4>
                <p>{app["description"]}</p>
            </div>
            ''', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<br><br><a href="{app["url"]}" target="_blank"><button style="background: linear-gradient(45deg,#FF4B4B,#FF8C42); color:white; border:none; padding:0.7rem; border-radius:8px; width:100%; font-weight:bold;">Launch →</button></a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"**Last updated:** {datetime.now().strftime('%B %d, %Y')} • [GitHub](https://github.com/lisa-silva) • [LinkedIn](https://linkedin.com/in/lisa-silva-706649391)")

# Sidebar
with st.sidebar:
    st.markdown("### Portfolio Stats")
    st.metric("Live Apps", "21")
    st.metric("Categories", "5")
    st.metric("Success Rate", "100%")
    search = st.text_input("Search apps")
    if search:
        for app in [a for a in apps_data if search.lower() in a["name"].lower() or search.lower() in a["description"].lower()]:
            st.markdown(f"**{app['emoji']} {app['name']}** → [Open]({app['url']})")
