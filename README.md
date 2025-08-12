# 🎙️ Multi-Language Text-to-Speech Translator

Convert text into speech in multiple languages with optional translation.

---

## 🚀 Features

* 🌐 **Multi-language support** – choose your input and output languages
* 🔄 **Text translation** – powered by [deep\_translator](https://pypi.org/project/deep-translator/)
* 🗣️ **Text-to-Speech** – powered by [gTTS](https://pypi.org/project/gTTS/)
* 🎧 **Audio playback** – listen to translated text instantly
* 💾 **Download audio** – save the spoken file to your device

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment *(Optional but Recommended)*

```bash
# Mac / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App Locally

```bash
streamlit run se.py
```

---

## ☁️ Deployment on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Click **New app** → Select your repository
4. Set:

   * **Main file path:** `se.py`
5. Click **Deploy** 🎉

---

## 📌 Example

Input:

```
Hello, how are you?
```

Output:

* **Translated (Hindi)** → नमस्ते, आप कैसे हैं?
* **Speech** → MP3 file generated & playable in the browser

---
