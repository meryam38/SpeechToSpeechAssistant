import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Please speak something...")
        audio = recognizer.listen(source)
        st.info("Recognizing...")
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service."

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    # Save the audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tts.save(tmp_file.name)
        return tmp_file.name

st.title("Speech to Speech Assistant")
st.write("This app converts speech input into text and then reads it out loud.")

if st.button("Record Speech"):
    recognized_text = recognize_speech_from_microphone()
    st.success(f"You said: {recognized_text}")

    if recognized_text:
        audio_file = text_to_speech(recognized_text)
        st.audio(audio_file, format='audio/mp3')
