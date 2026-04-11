from fastapi import FastAPI
from curl_cffi import requests

app = FastAPI()

@app.post("/generate-audio")
def generate_audio(text: str):
    url = "https://api.elevenlabs.io/v1/text-to-speech/..."
    
    headers = {
        "xi-api-key": "YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    
    payload = {"text": text}

    # impersonate="chrome110" makes ElevenLabs think this is a real browser, 
    # completely bypassing the TLS fingerprinting issue.
    response = requests.post(url, json=payload, headers=headers, impersonate="chrome110")
    
    return response.content
