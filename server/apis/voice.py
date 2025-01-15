from elevenlabs import play
from elevenlabs.client import ElevenLabs
import soundfile as sf
import os

# la clé API
VOICE_API_KEY = "sk_3c3800006263a32ef684f63f6a10a2bdb54144ce91619d73"

# Initialiser le client Eleven Labs avec la clé API
client = ElevenLabs(
  api_key=VOICE_API_KEY,
)

# Fonction pour jouer l'audio généré
def playAudio(message):
    audio = client.generate(
        text=message,
        voice="Charlotte",
        model="eleven_multilingual_v2"
    )
    play(audio)

# Fonction pour générer l'audio et le retourner sous forme de bytes
def generateAudio(message):
    audio = client.generate(
        text=message,
        voice="Charlotte",
        model="eleven_multilingual_v2"
    )
    audio_bytes = b''.join(audio) 
    return audio_bytes
