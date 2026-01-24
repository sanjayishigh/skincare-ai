import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# --- FIX: Added base_url back for OpenRouter keys ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_routine(skin_type, concerns, product):
    prompt = f"""
    You are a dermatologist. Create a skincare routine.
    User Profile: Skin Type: {skin_type}, Concern: {concerns[0] if concerns else 'General'}
    Selected Product: {product.get('brand')} {product.get('product_type')} ({product.get('key_ingredient')})
    
    Task:
    1. Explain WHY {product.get('key_ingredient')} helps.
    2. Create a simple AM and PM routine.
    3. List key precautions.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"ROUTINE ERROR: {e}")
        return f"Error generating routine: {str(e)}"