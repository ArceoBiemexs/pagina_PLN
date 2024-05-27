import streamlit as st
from gtts import gTTS

def text_to_audio(text):
    tts = gTTS(text=text, lang='es')
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    audio_bytes = audio_file.read()
    return audio_bytes

def main():
    st.title("Conversor de Texto a Audio")
    text = st.text_area("Introduce el texto que deseas convertir a audio:")

    if st.button("Reproducir Audio"):
        if text:
            audio_bytes = text_to_audio(text)
            st.audio(audio_bytes, format='audio/mp3')
            st.success("Audio reproducido con éxito.")
        else:
            st.error("Por favor, introduce el texto que deseas convertir a audio.")

if __name__ == "__main__":
    main()
