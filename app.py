from flask import Flask, request, jsonify, send_from_directory
from recommender import recommend_products
from gpt_routine import generate_routine
from face_analyzer import analyze_face_image
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder="static")

# Disable Cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/analyze")
def analyze_page():
    return send_from_directory("static", "analyze.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

@app.route("/scan_face", methods=["POST"])
def scan_face():
    try:
        # Get JSON data (not file)
        data = request.json
        if not data or 'image' not in data:
            return jsonify({"error": "No image data received"}), 400
        
        # Send base64 string directly to analyzer
        result = analyze_face_image(data['image'])
        
        return jsonify(result)

    except Exception as e:
        print(f"SERVER ERROR: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        products = recommend_products(int(data.get("age", 25)), data.get("skin_type", ""), data.get("concern", ""), data.get("product_type", ""))
        return jsonify({"status": "success", "products": products})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/routine", methods=["POST"])
def routine():
    data = request.json
    return jsonify({"routine": generate_routine(data.get("skin_type"), [data.get("concern")], data.get("product"))})

if __name__ == "__main__":
    app.run(debug=True, port=5001)