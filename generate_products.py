# generate_products.py
import pandas as pd

products = pd.DataFrame([
    [1, "Boho Summer Top", "boho,summer,pastel", "tops", 90],
    [2, "Denim Jeans", "denim,casual", "bottoms", 85],
    [3, "Floral Skirt", "floral,summer,casual", "skirts", 88],
    [4, "Formal Shirt", "formal,office,white", "tops", 80],
    [5, "Beach Dress", "boho,beach,summer", "dresses", 95],
    [6, "Casual Hoodie", "casual,winter,warm", "outerwear", 75],
    [7, "Slim Fit Blazer", "formal,blazer,office", "jackets", 92],
    [8, "Graphic Tee", "casual,trendy,summer", "tops", 77],
    [9, "Leather Jacket", "leather,trendy,winter", "jackets", 93],
    [10, "Cotton Kurta", "ethnic,casual", "tops", 89]
], columns=["product_id", "title", "tags", "category", "popularity_score"])

products.to_csv("products.csv", index=False)
print("products.csv created.")


import pandas as pd

pd.DataFrame(columns=["user_id", "product_id", "action"]).to_csv("users.csv", index=False)
print("users.csv created.")
