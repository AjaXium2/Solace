from elevenlabs import play
from elevenlabs.client import ElevenLabs
import soundfile as sf
import os

VOICE_API_KEY = os.getenv("VOICE_API_KEY")

client = ElevenLabs(
  api_key=VOICE_API_KEY,
)

def playAudio(message):
    audio = client.generate(
        text=message,
        voice="Charlotte",
        model="eleven_multilingual_v2"
    )
    play(audio)

def generateAudio(message):
    audio = client.generate(
        text=message,
        voice="Charlotte",
        model="eleven_multilingual_v2"
    )
    audio_bytes = b''.join(audio) 
    return audio_bytes