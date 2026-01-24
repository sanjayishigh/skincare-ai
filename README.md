# ✨ AI Skincare Recommender & Face Analyzer

A sophisticated web application that analyzes facial images to provide personalized skincare routines and product recommendations based on your unique skin needs. Powered by **Python 3.12** and **OpenAI** (via OpenRouter).

---

## 🚀 Features

- **Face Analysis** — Upload an image to detect skin type and concerns
- **AI Routine Generation** — Custom AM/PM routines generated via GPT models
- **Product Recommender** — Intelligent matching of products to your unique skin profile
- **Flask Backend** — Robust and lightweight web server implementation

---

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Framework:** Flask
- **AI/ML:** OpenAI (OpenRouter API), Pandas, Pillow (PIL)
- **Environment:** Dotenv for secure configuration

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

**Activate it:**

- **Windows:**
```bash
  venv\Scripts\activate
```

- **macOS / Linux:**
```bash
  source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration (Required)

> ⚠️ **This application requires an OpenRouter API key to function.**

### Create a `.env` File

In the project root (same directory as `app.py`), create a file named `.env`:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### Alternative: Set Environment Variable Manually

**CMD:**
```cmd
set OPENROUTER_API_KEY=your_openrouter_api_key_here
```

**PowerShell:**
```powershell
$env:OPENROUTER_API_KEY="your_openrouter_api_key_here"
```

---

## 🚀 Running the Application
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 💡 Usage Flow

1. Upload a facial image
2. Image is processed by `face_analyzer.py`
3. Skin attributes are passed to the GPT routine generator
4. Personalized skincare routine and product suggestions are returned

---

## 📁 Project Structure
```
├── app.py               # Flask app entry point
├── face_analyzer.py     # Facial image processing logic
├── gpt_routine.py       # OpenRouter / GPT integration
├── recommender.py       # Product recommendation logic
├── requirements.txt     # Python dependencies
├── .env                 # API keys (DO NOT COMMIT)
├── static/              # CSS, JS, uploaded images
└── templates/           # HTML templates
```

---

## 🔒 Security Notes

> **Important:** Follow these security best practices:

- ❌ **Never commit `.env` files** to version control
- ✅ Ensure `.env` is listed in `.gitignore`
- 🔄 Rotate your API key immediately if exposed
- ⚠️ Failure to protect your API key can result in unauthorized usage and charges

---

## 📄 License

[Add your license here, e.g., MIT License]

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/your-repo-name/issues).

---

## 👤 Author

**Your Name**
- GitHub: [@sanjayishigh](https://github.com/sanjayishigh)

---

## ⭐ Show your support

Give a ⭐️ if this project helped you!
