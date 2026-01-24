# ✨ AI Skincare Recommender & Face Analyzer A sophisticated web application powered by **Python 3.12** and **OpenAI** (via OpenRouter). This project analyzes facial images to provide personalized skincare routines and product recommendations based on specific skin needs. --- ## 🚀 Features * **Face Analysis**: Upload an image to detect skin type and concerns. * **AI Routine Generation**: Custom AM/PM routines generated via GPT models. * **Product Recommender**: Intelligent matching of products to your unique skin profile. * **Flask Backend**: A robust and lightweight web server implementation. --- ## 🛠️ Tech Stack * **Language:** Python 3.12 * **Framework:** Flask * **AI/ML:** OpenAI (OpenRouter API), Pandas, Pillow (PIL) * **Environment:** Dotenv for secure configuration ---

#Installation & Setup
##1. Clone the Repository
`git clone https://github.com/your-username/your-repo-name.git`
`cd your-repo-name`

3#2. Create a Virtual Environment
`python -m venv venv`


###Activate it:

####Windows

`venv\Scripts\activate`


####macOS / Linux

`source venv/bin/activate`

##3. Install Dependencies
`pip install -r requirements.txt`

###Configuration (Required)

This application will not run without an OpenRouter API key.

####Create a .env File

In the project root (same directory as app.py), create a file named .env:

'OPENROUTER_API_KEY=your_openrouter_api_key_here'

####Optional: Set Environment Variable Manually

CMD

'set OPENROUTER_API_KEY=your_openrouter_api_key_here'


PowerShell

'$env:OPENROUTER_API_KEY="your_openrouter_api_key_here"'

##Running the Application
'python app.py'


##Open your browser and navigate to:

'http://127.0.0.1:5000'

Usage Flow

Upload a facial image.

Image is processed by face_analyzer.py.

Skin attributes are passed to the GPT routine generator.

Personalized skincare routine and product suggestions are returned.

#Project Structure
├── app.py               # Flask app entry point
├── face_analyzer.py     # Facial image processing logic
├── gpt_routine.py       # OpenRouter / GPT integration
├── recommender.py       # Product recommendation logic
├── requirements.txt     # Python dependencies
├── .env                 # API keys (DO NOT COMMIT)
├── static/              # CSS, JS, uploaded images
└── templates/           # HTML templates (if used)

Security Notes

Never commit .env files
Ensure .env is listed in .gitignore
Rotate your API key immediately if exposed
Failure to do this will get your API key abused.
