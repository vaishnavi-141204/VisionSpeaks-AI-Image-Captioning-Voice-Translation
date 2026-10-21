import os
import uuid
from flask import Flask, render_template, request, session, send_from_directory
from transformers import BlipProcessor, BlipForConditionalGeneration
from googletrans import Translator
from gtts import gTTS
from PIL import Image
import torch

# Disable GPU to avoid WinError 1114
os.environ["CUDA_VISIBLE_DEVICES"] = ""

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session

# Folders
UPLOAD_FOLDER = "uploads"
AUDIO_FOLDER = "static/audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

device = torch.device("cpu")

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)

translator = Translator()


# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/", methods=["GET", "POST"])
def index():
    caption = ""
    translated = ""
    audio_url = ""

    # Get the last uploaded image filename from session
    image_filename = session.get("image_filename", None)

    if request.method == "POST":
        image = request.files["image"]
        lang = request.form["language"]

        # Save uploaded image
        uid = str(uuid.uuid4())
        ext = os.path.splitext(image.filename)[1]
        filename = uid + ext
        image.save(os.path.join(UPLOAD_FOLDER, filename))

        # Store filename in session so it remains until refresh or new upload
        session["image_filename"] = filename
        image_filename = filename

        # Generate caption
        img = Image.open(os.path.join(UPLOAD_FOLDER, filename)).convert("RGB")
        inputs = processor(img, return_tensors="pt").to(device)
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)

        # Translate caption
        translated = translator.translate(caption, dest=lang).text

        # Generate audio
        audio_file = f"{uid}.mp3"
        audio_path = os.path.join(AUDIO_FOLDER, audio_file)
        gTTS(translated, lang=lang).save(audio_path)
        audio_url = os.path.join("static/audio", audio_file)

    return render_template(
        "index.html",
        image_filename=image_filename,
        caption=caption,
        translated=translated,
        audio=audio_url
    )


if __name__ == "__main__":
    app.run(debug=True)