# VisionSpeak – AI-Powered Image Captioning and Voice Translating System

## About the Project

VisionSpeak is an AI-powered web application that generates captions for uploaded images, translates the captions into a selected language, and converts the translated text into speech. It combines computer vision, natural language processing, and text-to-speech technology to improve accessibility.

## Features

- Upload images through a web interface.
- Generate image captions using the BLIP model.
- Translate captions into a selected language.
- Convert translated text into speech.
- Play generated audio directly in the browser.
- Run the application using CPU processing.

## Technologies Used

- Python
- Flask
- Hugging Face Transformers (BLIP)
- PyTorch
- Pillow (PIL)
- Googletrans
- gTTS
- HTML and CSS

## How It Works

1. Upload an image.
2. Generate an English caption using BLIP.
3. Translate the caption into the selected language.
4. Convert the translated caption into speech.
5. View the caption and translation, and play the audio.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the placeholders with your repository URL and folder name.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open this address in your browser:

http://127.0.0.1:5000/

The first run may take longer because the pretrained BLIP model must be downloaded.

## Project Structure

```text
VisionSpeak/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── audio/
└── uploads/
```

Make sure the folders match the paths used in your Python code.

## Requirements

- Python 3.10 or later
- pip
- Internet connection for model downloads and online translation and speech services
- Recommended RAM: 8 GB or more

## Future Enhancements

- Support for additional languages.
- Real-time image and video captioning.
- Improved caption generation speed.
- Mobile application support.
- Enhanced accessibility features.

## Author

Vaishnavi S
