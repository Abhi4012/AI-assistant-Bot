import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    st.title("AI Assistant")
    st.markdown(
        """
        <style>
        .title {
            color: #008080;
            text-align: center;
        }
        .btn {
            background-color: #008080;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #006666;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            audio_file = open("speech.mp3", "rb")
            audio_bytes = audio_file.read()

            st.subheader("Response:")
            st.text_area(label="", value=response, height=350)

            st.subheader("Audio Response:")
            st.audio(audio_bytes, format="audio/mp3")

            st.markdown(
                """
                <a href="data:audio/mp3;base64,{0}" download="speech.mp3">
                <button class="btn">Download Speech</button>
                </a>
                """.format(audio_bytes.hex()),
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()

