# YouTube Audio Transcriber with Whisper AI

This Streamlit application allows users to download audio from YouTube videos and transcribe it using Whisper AI. The transcription results in `.srt`, `.txt`, and `.tsv` files, which can be viewed and downloaded directly from the app.

## Features

- Transcribe YouTube videos with url.
- Support for various Whisper AI models.
- View and download transcription files in `.srt`, `.txt`, and `.tsv` formats.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rishabh11336/Youtube-Subtitle.git
    cd your-repo-name
    ```

2. Install the required Python packages:
    ```bash
    pip install streamlit pytube pydub openai-whisper
    ```

## Usage

1. Ensure requirements.txt is installed and accessible from the command line:
    ```bash
    pip install -r requirements.txt
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

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and inference speed relative to the large model; actual speed may vary depending on many factors including the available hardware.

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

The `.en` models for English-only applications tend to perform better, especially for the `tiny.en` and `base.en` models. We observed that the difference becomes less significant for the `small.en` and `medium.en` models.  


## Project Structure

Youtube-Subtitle/  
├── app.py  
├── README.md  
└── requirements.txt  


- `app.py`: Main application file containing the Streamlit app code.
- `README.md`: This README file.
- `requirements.txt`: List of required Python packages.


## Example

1. Enter the YouTube URL.
2. Select the Whisper AI model.
3. Click "Download and Transcribe".
4. View and download the transcription files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.