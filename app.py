import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import os
import subprocess

def download_youtube_audio(url, save_path='.', filename='audio'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the audio stream with the highest bitrate
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        # Download the audio to the specified path
        temp_file = audio_stream.download(output_path=save_path, filename='temp_audio')

        # Convert the downloaded file to mp3
        audio = AudioSegment.from_file(temp_file)
        mp3_path = os.path.join(save_path, f"{filename}.mp3")
        audio.export(mp3_path, format="mp3")

        # Remove the temporary file
        os.remove(temp_file)

        return mp3_path
    except Exception as e:
        return str(e)

def transcribe_audio_with_whisper(audio_path, model_type):
    try:
        # Run the Whisper CLI command
        command = f"whisper {audio_path} --model {model_type}"
        subprocess.run(command, shell=True, check=True)

        # Get the paths of the generated files
        base_filename = os.path.splitext(audio_path)[0]
        srt_path = f"{base_filename}.srt"
        txt_path = f"{base_filename}.txt"
        tsv_path = f"{base_filename}.tsv"

        return srt_path, txt_path, tsv_path
    except Exception as e:
        return str(e), None, None

# Streamlit app
st.title('YouTube Audio Transcriber with Whisper AI')

url = st.text_input('Enter the YouTube URL')
filename = st.text_input('Enter the desired filename (without extension)', 'audio')

model_type = st.selectbox(
    'Select Whisper AI Model Type',
    [
        "tiny.en", "tiny", "base.en", "base", "small.en", "small",
        "medium.en", "medium", "large"
    ]
)

if st.button('Download and Transcribe'):
    if url:
        with st.spinner('Downloading and converting...'):
            save_path = '.'
            audio_path = download_youtube_audio(url, save_path, filename)
            if os.path.exists(audio_path):
                st.success(f'Download completed! Audio saved to: {audio_path}')
                
                with st.spinner('Transcribing with Whisper AI...'):
                    srt_path, txt_path, tsv_path = transcribe_audio_with_whisper(audio_path, model_type)
                    if srt_path and os.path.exists(srt_path):
                        st.success('Transcription completed!')
                        
                        with open(srt_path, 'r') as file:
                            srt_content = file.read()
                        with open(txt_path, 'r') as file:
                            txt_content = file.read()
                        with open(tsv_path, 'r') as file:
                            tsv_content = file.read()

                        st.download_button(label="Download SRT", data=srt_content, file_name=f"{filename}.srt")
                        st.download_button(label="Download TXT", data=txt_content, file_name=f"{filename}.txt")
                        st.download_button(label="Download TSV", data=tsv_content, file_name=f"{filename}.tsv")

                        st.text_area("SRT Content", srt_content, height=200)
                        st.text_area("TXT Content", txt_content, height=200)
                        st.text_area("TSV Content", tsv_content, height=200)
                    else:
                        st.error(f'An error occurred during transcription: {srt_path}')
            else:
                st.error(f'An error occurred during download: {audio_path}')
    else:
        st.warning('Please enter a valid YouTube URL')
