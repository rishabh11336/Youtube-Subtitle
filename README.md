# YouTube Audio Transcriber with Whisper AI

This Streamlit application allows users to download audio from YouTube videos and transcribe it using Whisper AI. The transcription results in `.srt`, `.txt`, and `.tsv` files, which can be viewed and downloaded directly from the app.

## Features

- Download audio from YouTube videos.
- Transcribe the audio using Whisper AI.
- Support for various Whisper AI models.
- View and download transcription files in `.srt`, `.txt`, and `.tsv` formats.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required Python packages:
    ```bash
    pip install streamlit pytube pydub openai-whisper
    ```

## Usage

1. Ensure Whisper AI is installed and accessible from the command line:
    ```bash
    pip install openai-whisper
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the app.

## How It Works

1. **Enter the YouTube URL:** Input the URL of the YouTube video you want to download the audio from.
2. **Enter the desired filename:** Specify the filename (without extension) for the downloaded audio file.
3. **Select the Whisper AI model:** Choose the desired Whisper AI model for transcription from the dropdown menu.
4. **Download and Transcribe:** Click the "Download and Transcribe" button to start the process.
5. **View and Download Transcription Files:** Once the transcription is complete, you can view and download the `.srt`, `.txt`, and `.tsv` files.

## Project Structure

your-repo-name/
├── app.py
├── README.md
└── requirements.txt


- `app.py`: Main application file containing the Streamlit app code.
- `README.md`: This README file.
- `requirements.txt`: List of required Python packages.

## Requirements

- Python 3.6 or higher
- Streamlit
- PyTube
- pydub
- openai-whisper

## Example

1. Enter the YouTube URL.
2. Enter the desired filename.
3. Select the Whisper AI model.
4. Click "Download and Transcribe".
5. View and download the transcription files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.