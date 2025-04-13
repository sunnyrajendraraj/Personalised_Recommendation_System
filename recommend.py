# recommend.py
import pandas as pd
from visualize import plot_user_profile, plot_recommendation_scores
from utils import (
    cold_start_recommendations,
    simulate_user_clicks,
    build_user_profile,
    personalized_recommendations
)

# Load products
products = pd.read_csv("products.csv")

print("\n--- ROUND 1: Cold Start Recommendations ---")
round1 = cold_start_recommendations(products)
print(round1[["product_id", "title"]])

# Simulate user clicks
clicked_ids = [5, 8]  # Simulated clicked items
interactions = simulate_user_clicks(user_id=1, clicked_product_ids=clicked_ids)
print("\nUser clicked:", clicked_ids)

# Build profile
profile = build_user_profile(products, clicked_ids)
print("\n--- UPDATED USER PROFILE ---")
print("Preferred tags:", profile["preferred_tags"])
print("Preferred categories:", profile["preferred_categories"])

# Visualize profile
plot_user_profile(profile)

# Round 2 recommendations
print("\n--- ROUND 2: Personalized Recommendations ---")
round2 = personalized_recommendations(products, profile)
print(round2[["product_id", "title", "score"]])

# Visualize score comparison
plot_recommendation_scores(round1, round2)
