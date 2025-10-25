import streamlit as st

def record_audio(filename="response.wav", duration=10):
    st.info(f"🎤 Please start recording. Suggested: {duration} seconds")
    audio_data = st.audio_input("🎙️ Tap to record your response")

    if audio_data:
        with open(filename, "wb") as f:
            f.write(audio_data.getvalue())
        st.success(f"✅ Audio saved as: {filename}")
        st.audio(audio_data)
        return filename

    return None


