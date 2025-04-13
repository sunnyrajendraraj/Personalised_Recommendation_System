# app.py

import streamlit as st
import pandas as pd
from utils import *
from visualize import *

# Load Data
products = pd.read_csv("products.csv")
st.set_page_config(page_title="AI Shopping Recommender", layout="wide")

st.title("🛍️ Personalized Shopping Recommendation System")
st.markdown("This app evolves its recommendations based on your interactions.")

st.header("🔍 Round 1: Cold Start Recommendations")
cold_recs = cold_start_recommendations(products)
st.dataframe(cold_recs[["product_id", "title", "category", "popularity_score"]], use_container_width=True)

# Simulate click input
st.header("🖱️ Simulate User Clicks")
clicked_titles = st.multiselect(
    "Select products you like:",
    cold_recs["title"].tolist()
)

if clicked_titles:
    clicked_ids = products[products["title"].isin(clicked_titles)]["product_id"].tolist()
    st.success(f"You clicked: {clicked_titles}")

    # Update user profile
    profile = build_user_profile(products, clicked_ids)
    st.header("🧠 User Profile (Knowledge Graph)")
    st.write("Preferred Tags:", profile["preferred_tags"])
    st.write("Preferred Categories:", profile["preferred_categories"])
    plot_user_profile(profile)

    # Personalized Recommendations
    st.header("🎯 Round 2: Personalized Recommendations")
    personalized = personalized_recommendations(products, profile)
    st.dataframe(personalized[["product_id", "title", "category", "score"]], use_container_width=True)

    # Visualize comparison
    plot_recommendation_scores(cold_recs, personalized)
else:
    st.warning("Please select a few products to simulate clicks.")
