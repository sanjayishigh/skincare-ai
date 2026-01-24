import os
import base64
import json
import io
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# --- FIX: Added base_url back for OpenRouter keys ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_face_image(base64_string):
    try:
        if "," in base64_string:
            header, encoded = base64_string.split(",", 1)
        else:
            encoded = base64_string

        # Decode & Fix PNG to JPG
        image_data = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(image_data))
        
        if image.mode in ('RGBA', 'P'):
            image = image.convert('RGB')

        image.thumbnail((800, 800))
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=85)
        optimized_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        prompt = """
        You are a dermatologist AI. Analyze this face image.
        Output strictly valid JSON with these keys:
        {
            "skin_type_estimate": "Oily/Dry/Combination/Normal/Sensitive",
            "detected_issues": ["List", "top", "visible", "issues", "or", "None Visible"],
            "analysis": "Professional 2-sentence summary."
        }
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini", # OpenRouter supports this model name too
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{optimized_base64}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=300
        )
        
        content = response.choices[0].message.content
        content = content.replace("```json", "").replace("```", "").strip()
        data = json.loads(content)

        if not data.get("detected_issues"):
            data["detected_issues"] = ["None Visible"]
            
        return data

    except Exception as e:
        print(f"AI ERROR: {e}")
        return {
            "skin_type_estimate": "Error",
            "detected_issues": ["Connection Failed"],
            "analysis": f"API Error: {str(e)}"
        }