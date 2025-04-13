# utils.py

import pandas as pd
from collections import Counter

def cold_start_recommendations(products, top_n=5):
    return products.sort_values(by="popularity_score", ascending=False).head(top_n)

def simulate_user_clicks(user_id, clicked_product_ids):
    return pd.DataFrame({
        "user_id": [user_id] * len(clicked_product_ids),
        "product_id": clicked_product_ids,
        "action": ["click"] * len(clicked_product_ids)
    })

def build_user_profile(products, clicked_ids):
    clicked_products = products[products["product_id"].isin(clicked_ids)]
    tags = []
    categories = []
    for _, row in clicked_products.iterrows():
        tags.extend(row["tags"].split(','))
        categories.append(row["category"])
    tag_counter = Counter(tags)
    cat_counter = Counter(categories)
    return {
        "preferred_tags": [tag for tag, _ in tag_counter.most_common(3)],
        "preferred_categories": [cat for cat, _ in cat_counter.most_common(2)]
    }

def personalized_recommendations(products, user_profile, top_n=5):
    def score(row):
        tag_score = len(set(row["tags"].split(',')) & set(user_profile["preferred_tags"]))
        cat_score = 1 if row["category"] in user_profile["preferred_categories"] else 0
        return tag_score + cat_score + row["popularity_score"] / 100
    products["score"] = products.apply(score, axis=1)
    return products.sort_values(by="score", ascending=False).head(top_n)
