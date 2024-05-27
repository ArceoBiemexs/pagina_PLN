import streamlit as st
import pyttsx3

def text_to_audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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

