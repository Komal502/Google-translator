🌍 Text-to-Speech Translator App
A simple Streamlit web app that lets you:
✅ Translate text from one language to another using Google Translator API (deep_translator)
✅ Convert translated text into speech (Text-to-Speech)
✅ Download the generated audio file
✅ Runs directly in your browser after deployment on Streamlit Cloud

🚀 Features
Multi-language support – choose your input and output languages

Text translation – powered by deep_translator

Text-to-Speech – powered by gTTS

Audio playback – listen to translated text

Download audio – save the spoken file to your device

🛠️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the App Locally
bash
Copy
Edit
streamlit run se.py
📦 Deployment on Streamlit Cloud
Push your code to GitHub

Go to Streamlit Cloud

Click New app → select your repository

Set:

Main file path: se.py

Python version: (e.g., 3.9)

Click Deploy 🎉

📂 Project Structure
bash
Copy
Edit
📦 your-repo-name
 ┣ 📜 se.py               # Main Streamlit app file
 ┣ 📜 requirements.txt    # Python dependencies
 ┣ 📜 runtime.txt         # Python runtime version for deployment
 ┣ 📜 README.md           # Project documentation
 ┗ 📜 LICENSE             # (Optional) License file
📝 Requirements
streamlit

gtts

deep_translator

🎯 Usage
Select input and output languages from dropdowns

Type the text you want to translate

Click Translate

Listen to the translated text via audio player

Click Download Audio to save the file

📄 License
This project is licensed under the MIT License – you are free to use, modify, and share it.