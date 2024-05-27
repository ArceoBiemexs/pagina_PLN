import streamlit as st
from gtts import gTTS
import os

def text_to_audio(text):
    tts = gTTS(text=text, lang='es')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")

def main():
    st.title("Conversor de Texto a Audio")
    text = st.text_area("Introduce el texto que deseas convertir a audio:")

    if st.button("Reproducir Audio"):
        if text:
            text_to_audio(text)
            st.success("Audio reproducido con éxito.")
        else:
            st.error("Por favor, introduce el texto que deseas convertir a audio.")

if __name__ == "__main__":
    main()
