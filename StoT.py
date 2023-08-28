import streamlit as st
import sounddevice as sd
import numpy as np
import wavio
import whisper
import os

def record_audio(output_filename, duration, sample_rate):
    st.write("Recording...")
    audio_data = sd.rec(int(duration * sample_rate),
                        samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until recording is finished
    st.write("Recording finished.")

    # Save the recorded audio to a WAV file
    wavio.write(output_filename, audio_data, sample_rate, sampwidth=2)

def main():
    st.title("Speech-to-Text using Whisper and Streamlit")
    
    # Sidebar input for recording duration
    recording_duration = st.sidebar.slider("Recording Duration (seconds)", 1, 10, 5)
    
    # Record audio button
    if st.sidebar.button("Record Audio"):
        output_file = "recorded_audio.wav"  # Specify the output file name
        sample_rate = 44100  # Sampling rate (samples per second)

        record_audio(output_file, recording_duration, sample_rate)
        st.sidebar.write("Audio saved as:", output_file)
        
        # Verify if the audio file exists
        if os.path.exists(output_file):
            # Load the Whisper model
            model = whisper.load_model('base')

            # Transcribe the audio using the loaded model
            text = model.transcribe(output_file)
            
            # Display the transcribed text
            st.write("Transcribed Text:", text['text'])
        else:
            st.sidebar.write("Audio file not found.")
    
if __name__ == "__main__":
    main()
