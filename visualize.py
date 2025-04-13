# visualize.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_user_profile(profile):
    """Bar plots for preferred tags and categories"""
    tags = profile["preferred_tags"]
    categories = profile["preferred_categories"]

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    tag_df = pd.DataFrame({'Tag': tags, 'Importance': [1]*len(tags)})
    sns.barplot(data=tag_df, x='Tag', y='Importance', palette='pastel')
    plt.title("Preferred Tags")

    plt.subplot(1, 2, 2)
    cat_df = pd.DataFrame({'Category': categories, 'Importance': [1]*len(categories)})
    sns.barplot(data=cat_df, x='Category', y='Importance', palette='muted')
    plt.title("Preferred Categories")

    plt.tight_layout()
    plt.show()

def plot_recommendation_scores(round1_df, round2_df):
    """Compare scores before and after personalization"""
    round1_df["round"] = "Cold Start"
    round1_df["score"] = round1_df["popularity_score"] / 100  # Cold start doesn't have personalized score

    round2_df["round"] = "Personalized"

    df_combined = pd.concat([
        round1_df[["title", "score", "round"]],
        round2_df[["title", "score", "round"]]
    ])

    plt.figure(figsize=(12, 5))
    sns.barplot(data=df_combined, x="title", y="score", hue="round", palette="Set2")
    plt.title("Recommendation Scores: Cold Start vs Personalized")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
