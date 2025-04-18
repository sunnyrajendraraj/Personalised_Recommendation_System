import streamlit as st
import pandas as pd
import os
import json
from PIL import Image
from utils import *
from visualize import *
from auth import authenticate, register_user

# ✅ Set config FIRST
st.set_page_config(page_title="📚 AI Hindi Book Recommender", layout="wide")

# --- Authentication Sidebar ---
st.sidebar.title("🔐 Login / Register")
auth_mode = st.sidebar.radio("Choose option", ["Login", "Register"])

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if auth_mode == "Login":
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.sidebar.success(f"✅ Logged in as {username}")
        else:
            st.sidebar.error("❌ Invalid username or password.")
elif auth_mode == "Register":
    if st.sidebar.button("Register"):
        if register_user(username, password):
            st.sidebar.success("🎉 Registered successfully! Now login.")
        else:
            st.sidebar.error("⚠️ Username already exists.")

# --- Access Control ---
if not st.session_state.get("logged_in", False):
    st.warning("🚫 Please login to access the recommendation system.")
    st.stop()

user_id = st.session_state["user"]

# --- Load Product Data ---
if not os.path.exists("products.csv"):
    st.error("❌ 'products.csv' not found. Please add it to the project directory.")
    st.stop()

products = pd.read_csv("products.csv")

st.title("Hindi Book Recommendation System")
st.markdown("This app evolves its recommendations based on your interactions.")

# --- Cold Start Recommendations ---
st.header("🔍 Round 1: Cold Start Recommendations")
cold_recs = cold_start_recommendations(products)

# --- Display Product Thumbnails (150x150 grid) ---
st.subheader("🖼️ Book Thumbnails")
image_folder = './data/images'
thumbnail_width, thumbnail_height = 150, 150
cols = st.columns(5)

for idx, (index, row) in enumerate(cold_recs.iterrows()):
    product_id = row["product_id"]
    image_path = os.path.join(image_folder, f"{product_id}.jpg")
    
    with cols[idx % 5]:
        if os.path.exists(image_path):
            img = Image.open(image_path).convert("RGB")
            img = img.resize((thumbnail_width, thumbnail_height))
            st.image(img, use_container_width=True)
        else:
            placeholder_img = Image.new('RGB', (thumbnail_width, thumbnail_height), color='gray')
            st.image(placeholder_img, use_container_width=True)

        st.markdown(f"**{row['title']}**")
        st.caption(f"Category: {row['category']}")
        st.caption(f"Popularity: ⭐ {row['popularity_score']}")

# --- Cold Recommendation Data ---
st.dataframe(cold_recs[["product_id", "title", "category", "popularity_score"]], use_container_width=True)

# --- Simulate Click Input ---
st.header("🖱️ Simulate User Clicks")
clicked_titles = st.multiselect(
    "Select products you like:",
    cold_recs["title"].tolist()
)

if clicked_titles:
    clicked_ids = products[products["title"].isin(clicked_titles)]["product_id"].tolist()
    st.success(f"You clicked: {clicked_titles}")

    # --- Build User Profile ---
    profile = build_user_profile(products, clicked_ids)
    st.header("🧠 User Profile (Knowledge Graph)")
    st.write("Preferred Tags:", profile["preferred_tags"])
    st.write("Preferred Categories:", profile["preferred_categories"])
    plot_user_profile(profile)

    # --- Personalized Recommendations ---
    st.header("🎯 Round 2: Personalized Recommendations")
    personalized = personalized_recommendations(products, profile)
    st.dataframe(personalized[["product_id", "title", "category", "score"]], use_container_width=True)

    # --- Visualize Comparison ---
    plot_recommendation_scores(cold_recs, personalized)

    # --- Simulate & Store User Interaction ---
    new_interaction = simulate_user_clicks(user_id, clicked_ids)
    if os.path.exists("data/users.csv"):
        users_df = pd.read_csv("data/users.csv")
        users_df = pd.concat([users_df, new_interaction], ignore_index=True)
    else:
        os.makedirs("data", exist_ok=True)
        users_df = new_interaction
    users_df.to_csv("data/users.csv", index=False)

    # --- Hybrid Recommendations ---
    st.header("🔀 Final Round: Hybrid Recommendations")
    content_recs = personalized_recommendations(products, profile, top_n=10)
    collab_recs = collaborative_recommendations(products, users_df, user_id, top_n=5)

    final_recs = pd.concat([content_recs, collab_recs]).drop_duplicates("product_id").head(5)
    st.dataframe(final_recs[["product_id", "title", "category", "score"]], use_container_width=True)
else:
    st.warning("⚠️ Please select a few products to simulate clicks.")
