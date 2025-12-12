import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AKELNY | AI Nutrition", page_icon="🥗", layout="wide")

# --- HEADER (Matching your Poster Info) ---
st.title("🇪🇬 AKELNY: Localized AI-Powered Nutrition")
st.markdown("""
**Student:** Youssef Hany Koheil – CU2500980  
**Module:** Introduction to Business Management (KH3124SSL) | **Year:** 2025  
*Vertical: AI Diet Planning, Local Recipe Recognition, Smart Grocery Integration*
""")
st.markdown("---")

# --- SIDEBAR: USER PROFILE ---
st.sidebar.header("👤 User Profile")
name = st.sidebar.text_input("Name", "Youssef")
goal = st.sidebar.selectbox("Goal", ["Lose Weight", "Gain Muscle", "Maintain"])
diet_type = st.sidebar.selectbox("Diet Preference", ["Standard", "Vegetarian", "Egyptian Local (Baladi)"])
budget = st.sidebar.slider("Weekly Grocery Budget (EGP)", 500, 5000, 1500)

if st.sidebar.button("Generate AI Plan"):
    st.session_state['generated'] = True
else:
    if 'generated' not in st.session_state:
        st.session_state['generated'] = False

# --- TABS FOR THE 3 PILLARS ---
tab1, tab2, tab3 = st.tabs(["🧬 AI Diet Planner", "🛒 Smart Grocery", "📈 Admin KPIs"])

# --- TAB 1: AI DIET PLANNING ---
with tab1:
    st.subheader(f"Thinking for {name}...")
    
    if st.session_state['generated']:
        # Mock AI Logic based on Local Preference
        if diet_type == "Egyptian Local (Baladi)":
            breakfast = "Ful Medames with Flaxseed Oil (300 kcal)"
            lunch = "Koshary (Small portion, extra lentils) (450 kcal)"
            dinner = "Yoghurt with Honey & Fruits (200 kcal)"
        else:
            breakfast = "Oatmeal with Berries (350 kcal)"
            lunch = "Grilled Chicken Breast with Rice (500 kcal)"
            dinner = "Greek Salad (250 kcal)"

        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"**Breakfast**\n\n🍳 {breakfast}")
        with col2:
            st.success(f"**Lunch**\n\n🍲 {lunch}")
        with col3:
            st.warning(f"**Dinner**\n\n🥣 {dinner}")
            
        st.caption("✅ AI has adjusted portions to fit your calorie deficit.")
    else:
        st.write("👈 Click 'Generate AI Plan' in the sidebar to start.")

# --- TAB 2: SMART GROCERY INTEGRATION ---
with tab2:
    st.subheader("🛒 Localized Smart Grocery List")
    
    # Mock Data for Grocery Integration
    data = {
        "Ingredient": ["Egyptian Rice (1kg)", "Lentils (500g)", "Tomato Sauce", "Local Baladi Bread", "Chicken Breast (1kg)"],
        "Supermarket": ["Spinneys", "Carrefour", "Kazyon", "Local Bakery", "Gourmet"],
        "Price (EGP)": [35, 45, 15, 10, 220],
        "In Stock": [True, True, True, True, False]
    }
    df = pd.DataFrame(data)
    
    # Filter based on diet
    if st.session_state['generated']:
        st.table(df)
        total_price = df["Price (EGP)"].sum()
        
        c1, c2 = st.columns([2, 1])
        with c1:
            st.metric(label="Total Cart Value", value=f"{total_price} EGP")
        with c2:
            if total_price > budget:
                st.error(f"Over Budget by {total_price - budget} EGP")
            else:
                st.success("Within Budget ✅")
        
        st.button("🚀 Checkout via Spinneys Integration")
    else:
        st.write("Generate a diet plan first to see your grocery list.")

# --- TAB 3: ADMIN & KPIS (From Poster Q5) ---
with tab3:
    st.subheader("📊 Strategic & Financial Control Dashboard")
    
    # Mock KPI Data
    kpi1, kpi2, kpi3 = st.columns(3)
    
    with kpi1:
        st.metric(label="Customer Acquisition Cost (CAC)", value="50 EGP", delta="-5% (Efficient)")
    with kpi2:
        st.metric(label="Lifetime Value (LTV)", value="450 EGP", delta="Ratio 9:1")
    with kpi3:
        st.metric(label="Churn Rate", value="2.1%", delta="-0.5% (Retained)")

    st.markdown("### Operational Velocity")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Tech Squad', 'Growth Squad', 'Ops Squad'])
    st.line_chart(chart_data)
    st.caption("Real-time squad velocity tracking (Agile/DevOps)")