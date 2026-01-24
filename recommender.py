import pandas as pd
import os

def load_data():
    if os.path.exists("ds.csv"):
        try:
            df = pd.read_csv("ds.csv")
            # Normalize column names (remove spaces, lowercase)
            df.columns = df.columns.str.strip().str.lower()
            return df.fillna("")
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return pd.DataFrame()
    return pd.DataFrame()

df = load_data()

def is_age_appropriate(user_age, range_str):
    """
    Checks if a user's age falls into range strings like '18-25', '56+', etc.
    """
    try:
        user_age = int(user_age)
        range_str = str(range_str).strip()
        
        if "+" in range_str:
            min_age = int(range_str.replace("+", ""))
            return user_age >= min_age
        
        if "-" in range_str:
            parts = range_str.split("-")
            min_age = int(parts[0])
            max_age = int(parts[1])
            return min_age <= user_age <= max_age
            
        return True # If data is weird, don't filter it out
    except:
        return True

def recommend_products(age, skin_type, concern, product_type):
    if df.empty:
        return []

    # Filter 1: Strict Product Type Match (e.g., only show Cleansers)
    # We use fuzzy string matching in case of capitalization differences
    filtered_df = df[df['product_type'].str.contains(product_type, case=False, na=False)].copy()

    results = []

    for _, row in filtered_df.iterrows():
        score = 0
        
        # Data from row
        p_skin = str(row.get("skin_type", "")).lower()
        p_concern = str(row.get("primary_concern", "")).lower()
        p_age_group = str(row.get("age_group", ""))
        p_rating = float(row.get("rating", 0))

        # 1. Skin Type Match (High Priority)
        if skin_type in p_skin or "all" in p_skin:
            score += 10

        # 2. Concern Match (High Priority)
        if concern in p_concern:
            score += 10

        # 3. Age Group Match
        if is_age_appropriate(age, p_age_group):
            score += 5

        # 4. Rating Boost (Add raw rating to score)
        score += p_rating

        # Only return products with some relevance
        if score > 0:
            # Since your CSV has no images, we generate a placeholder based on Brand Name
            brand_name = row.get("brand", "Unknown")
            img_url = f"https://placehold.co/300x200/FFC0CB/444444?text={brand_name}"

            results.append({
                "brand": row.get("brand"),
                "product_type": row.get("product_type"),
                "price": row.get("price_inr"),
                "rating": row.get("rating"),
                "reviews": row.get("number_of_reviews"),
                "key_ingredient": row.get("key_ingredient"),
                "additional_ingredient": row.get("additional_ingredient"),
                "image_url": img_url,
                "score": score
            })

    # Sort by Score first, then by Rating
    results = sorted(results, key=lambda x: (x["score"], x["rating"]), reverse=True)
    
    return results[:6] # Return top 6