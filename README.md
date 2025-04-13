# Progressive Personalized Recommendation System

## Overview
This project simulates a lightweight recommendation engine that evolves as the user interacts with the system.

## Steps:
1. **Cold Start**: Recommendations based on content (tags/category) and popularity.
2. **User Interaction**: Simulated clicks on selected products.
3. **User Profile Update**: Preferred tags and categories derived from clicked products.
4. **Personalized Recommendations**: Next round based on user preferences and popularity.

## Recommendation Logic:
- **Content Filtering**: Tag/category matching.
- **Collaborative Filtering (Simulated)**: Uses `popularity_score` as a proxy.
- **User Profile**: Stored as a Python dictionary (`preferred_tags`, `preferred_categories`).

## File Structure:
- `products.csv`: Product data.
- `users.csv`: User actions (initially empty).
- `recommend.py`: Main execution script.
- `utils.py`: Modularized functions.
