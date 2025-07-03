from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper
import spacy
from utils import extract_activities, calculate_emissions

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models once at startup
whisper_model = whisper.load_model("base")
nlp = spacy.load("en_core_web_sm")

@app.post("/api/upload-audio")
async def upload_audio(audio: UploadFile = File(...)):
    # Save the uploaded file temporarily
    temp_audio_path = "temp.wav"
    with open(temp_audio_path, "wb") as f:
        f.write(await audio.read())

    # Transcribe audio
    result = whisper_model.transcribe(temp_audio_path)
    text = result["text"]

    # Extract activities and calculate emissions
    activities = extract_activities(text, nlp)
    emissions = calculate_emissions(activities)

    return {
        "transcription": text,
        "activities": activities,
        "emissions": emissions
    }
