import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech to Text using Streamlit")

    # Set the filename for the recorded audio
    filename = "recorded_audio.wav"

    # Set the recording duration in seconds
    recording_duration = 5

    # Initialize the recognizer
    r = sr.Recognizer()

    # Button to start recording
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.info("Recording audio... Speak now!")

            # Adjust for ambient noise before recording
            r.adjust_for_ambient_noise(source)

            # Record the audio for the specified duration
            audio_data = r.listen(source, timeout=recording_duration)
            st.success("Recording finished.")

        # Save the recorded audio to the specified filename
        with open(filename, "wb") as f:
            f.write(audio_data.get_wav_data())

        # Perform speech recognition on the recorded audio
        try:
            text = r.recognize_google(audio_data)
            st.write("Transcription:", text)
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError as e:
            st.error("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
