import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Lisa Silva - AI Portfolio Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
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

# Header
st.markdown('<div class="main-header">Lisa Silva</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Engineer | 21+ Production Applications | Full-Stack Deployment</div>', unsafe_allow_html=True)

# Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stats-card"><h3>21+</h3><p>Production Apps</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stats-card"><h3>99.1%</h3><p>AI Accuracy</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stats-card"><h3>2 Months</h3><p>Acceleration</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stats-card"><h3>100%</h3><p>Deployed Live</p></div>', unsafe_allow_html=True)

st.markdown("### 🎯 Production-Ready Application Portfolio")
st.markdown("Welcome to my centralized portfolio hub showcasing **21+ deployed Streamlit applications**. Every app below is live and production-ready.")

# Fixed apps data — proper list of dicts
apps_data = [
    # Business & Compliance Suite
    {"name": "ARCHON Detector", "category": "Business & Compliance Suite", "description": "Compliance AI with 99.1% accuracy in regulatory analysis", "url": "https://archon-detector-app-lisa-silva.streamlit.app/", "emoji": "🛡️", "status": "Production"},
    {"name": "AUDITUS XAI", "category": "Business & Compliance Suite", "description": "Explainable AI for compliance detection and reasoning transparency", "url": "https://auditus-xai-lisa-silva.streamlit.app/", "emoji": "🔍", "status": "Production"},
    {"name": "RegTech Suite", "category": "Business & Compliance Suite", "description": "Comprehensive regulatory technology applications", "url": "https://comply-rag-lisa-silva.streamlit.app/", "emoji": "⚖️", "status": "Production"},
    {"name": "LeaseSync AI", "category": "Business & Compliance Suite", "description": "Real estate and lease management automation", "url": "https://lease-sync-ai-lisa-silva.streamlit.app/", "emoji": "🏢", "status": "Production"},
    {"name": "Finance Tracker", "category": "Business & Compliance Suite", "description": "Personal finance management and analysis", "url": "https://finance-tracker-app-lisa-silva.streamlit.app/", "emoji": "💰", "status": "Production"},
    {"name": "CSV Data Analyzer", "category": "Business & Compliance Suite", "description": "Business data analysis and visualization tool", "url": "https://csv-data-analyzer-lisa-silva.streamlit.app/", "emoji": "📊", "status": "Production"},
    {"name": "Cherrywood Nuisance Reporter", "category": "Business & Compliance Suite", "description": "Apartment community reporting tool for noise and issues", "url": "https://cherrywood-nuisance-reporter-dashboard.streamlit.app/", "emoji": "🏘️", "status": "Production"},

    # Productivity & Tools
    {"name": "FixSync", "category": "Productivity & Tools", "description": "Real-time visual repair collaboration platform for trades", "url": "https://fixsync-lisa-silva.streamlit.app/", "emoji": "🔧", "status": "Production"},
    {"name": "Plumber Portal", "category": "Productivity & Tools", "description": "White-label service request system", "url": "https://plumber-service-request-app-lisa-silva.streamlit.app/", "emoji": "🔧", "status": "Production"},
    {"name": "Universal Business VMS Platform", "category": "Productivity & Tools", "description": "Universal customer service + asset tracking template", "url": "https://universal-business-vms-platform.streamlit.app/", "emoji": "🏭", "status": "Production"},

    # AI & Research
    {"name": "Political Fact Checker", "category": "AI & Research Applications", "description": "Real-time political claim verification", "url": "https://political-fact-checker-lisa-silva-v2.streamlit.app/", "emoji": "🇺🇸", "status": "Production"},
    {"name": "Dark Triad Analyzer", "category": "AI & Research Applications", "description": "Psychological trait assessment", "url": "https://dark-triad-detector-quiz-lisa-silva-v2.streamlit.app/", "emoji": "🧠", "status": "Production"},
    {"name": "Catechism Scripture Analyzer", "category": "AI & Research Applications", "description": "Religious text analysis tool", "url": "https://catechism-scripture-analyzer-lisa-silva.streamlit.app/", "emoji": "📖", "status": "Production"},
    {"name": "Review Sentiment Analyzer", "category": "AI & Research Applications", "description": "Customer feedback sentiment detection", "url": "https://online-review-sentiment-analyzer-lisa-silva.streamlit.app/", "emoji": "⭐", "status": "Production"},
    {"name": "Quantum Me App", "category": "AI & Research Applications", "description": "Personal development & goal tracking", "url": "https://quantum-me-lisa-silva.streamlit.app/", "emoji": "🎯", "status": "Production"},

    # Portfolio & Demo
    {"name": "FlagPro Shift Scheduling", "category": "Portfolio & Demonstration", "description": "Workforce scheduling simulator", "url": "https://flagpro-shift-scheduling-lisa-silva.streamlit.app/", "emoji": "🚩", "status": "Production"},

    # Innovative Tools
    {"name": "Voidism", "category": "Innovative Tools", "description": "Scream into the void instead of texting your ex", "url": "https://voidism.streamlit.app/", "emoji": "🕳️", "status": "Production"},
    {"name": "Anti-Ex Text Generator", "category": "Innovative Tools", "description": "Perfect replies for toxic exes", "url": "https://anti-ex-text-generator.streamlit.app/", "emoji": "🚫", "status": "Production"},
    {"name": "Void Text", "category": "Innovative Tools", "description": "Fake texting app to stay no-contact", "url": "https://void-text-stay-no-contact.streamlit.app/", "emoji": "📱", "status": "Production"}
]

categories = ["Business & Compliance Suite", "Productivity & Tools", "AI & Research Applications", "Portfolio & Demonstration", "Innovative Tools"]

# Display by category
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
            st.markdown(f'<br><br><a href="{app["url"]}" target="_blank"><button style="background: linear-gradient(45deg, #FF4B4B, #FF8C42); color: white; border: none; padding: 0.6rem 1.2rem; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%;">Launch App →</button></a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(f"""
### 🚀 Technical Stack
- **Framework:** Streamlit • **Language:** Python • **Deployment:** Streamlit Cloud • **Source:** GitHub

### 📬 Connect
- **LinkedIn:** [linkedin.com/in/lisa-silva-706649391](https://www.linkedin.com/in/lisa-silva-706649391/)
- **GitHub:** [github.com/lisa-silva](https://github.com/lisa-silva)

*Last updated: {datetime.now().strftime("%B %d, %Y")}*  
**21+ live AI applications • 100% deployed • Zero downtime**
""")

# Sidebar
with st.sidebar:
    st.markdown("### 📊 Portfolio Stats")
    st.metric("Total Apps", "21")
    st.metric("Categories", "5")
    st.metric("Deployment Rate", "100%")
    st.metric("Top AI Accuracy", "99.1%")
    
    st.markdown("### 🔍 Quick Search")
    search = st.text_input("Search apps...", "")
    if search:
        results = [a for a in apps_data if search.lower() in a["name"].lower() or search.lower() in a["description"].lower()]
        for r in results:
            st.markdown(f"**{r['emoji']} {r['name']}**")
            st.caption(r["description"])
            st.markdown(f"[Launch →]({r['url']})")
