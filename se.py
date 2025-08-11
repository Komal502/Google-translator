# app.py
import streamlit as st
from gtts import gTTS
from io import BytesIO
from deep_translator import GoogleTranslator

# --------------------
# Streamlit App Title
# --------------------
st.set_page_config(page_title="Text-to-Speech Translator", page_icon="🔊", layout="centered")
st.title("🔊 Text-to-Speech with Translation")
st.markdown("Convert text to speech with optional translation. Type text or upload a file.")

# --------------------
# Language Options (display name -> code)
# --------------------
LANGUAGES = {
    'English': 'en', 'Hindi': 'hi', 'Marathi': 'mr', 'Gujarati': 'gu', 'Tamil': 'ta',
    'Telugu': 'te', 'Bengali': 'bn', 'Punjabi': 'pa', 'Urdu': 'ur', 'Kannada': 'kn',
    'Malayalam': 'ml', 'French': 'fr', 'Spanish': 'es', 'German': 'de', 'Italian': 'it',
    'Japanese': 'ja', 'Korean': 'ko', 'Chinese (Simplified)': 'zh-cn'
}

# UI controls
src_lang_name = st.selectbox("Source Language (text language)", options=["Auto Detect"] + list(LANGUAGES.keys()))
target_lang_name = st.selectbox("Target Language (for speech & translation)", options=list(LANGUAGES.keys()))

# --------------------
# Text Input Section
# --------------------
text_input = st.text_area("Enter your text here:", height=180)

uploaded_file = st.file_uploader("Or upload a text file (.txt)", type=["txt"])
if uploaded_file is not None:
    try:
        text_input = uploaded_file.read().decode("utf-8")
    except Exception:
        st.error("Couldn't read the uploaded file. Make sure it's a UTF-8 encoded .txt file.")

# Voice speed option
slow = st.checkbox("Speak slowly (slow speed)")

# --------------------
# Generate TTS
# --------------------
if st.button("Convert to Speech"):
    if not text_input or not text_input.strip():
        st.warning("Please enter some text or upload a file.")
    else:
        try:
            # Prepare language codes
            src_code = "auto" if src_lang_name == "Auto Detect" else LANGUAGES[src_lang_name]
            tgt_code = LANGUAGES[target_lang_name]

            # Translate if source != target (if user selected Auto Detect, we'll still request translation)
            translated_text = text_input
            if src_code != tgt_code:
                try:
                    # GoogleTranslator supports source='auto'
                    translated_text = GoogleTranslator(source=src_code, target=tgt_code).translate(text_input)
                except Exception as te:
                    # translation failed: fallback to original text and show message
                    st.warning(f"Translation failed, using original text. ({te})")
                    translated_text = text_input

            # Show translated text
            if translated_text != text_input:
                st.success(f"Translated text ({target_lang_name}):")
                st.write(translated_text)
            else:
                st.info("Using original text (no translation performed).")

            # Create TTS audio
            tts = gTTS(text=translated_text, lang=tgt_code, slow=slow)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)

            # Play in browser
            st.audio(audio_buffer.getvalue(), format="audio/mp3")

            # Download button (use bytes)
            st.download_button(
                label="⬇️ Download Audio (MP3)",
                data=audio_buffer.getvalue(),
                file_name="speech.mp3",
                mime="audio/mp3"
            )

        except Exception as e:
            st.error(f"Error: {e}")
            st.write("If you're running on Streamlit Cloud, ensure requirements.txt includes deep-translator and gTTS.")
