import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech



def main():
    st.title("AI Assistant")

    if st.button("Ask me anything"):
        with st.spinner("Listenning...."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            audio_file = open("speech.mp3", "rb")
            audio_bytes = audio_file.read()

            st.text_area(label="Response:", value=response, height=350)

            st.audio(audio_bytes)
            st.download_button(label="Download speech", 
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3",
                               #key="download_button",
                               )
if __name__ == "__main__":
    main()