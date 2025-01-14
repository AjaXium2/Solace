from elevenlabs import play
from elevenlabs.client import ElevenLabs
import soundfile as sf
import os

# Définir directement la clé API (pas besoin d'utiliser set ici)
VOICE_API_KEY = "sk_e26404d74b6c4c02cbcb526ccac90a0323a58512152ff57e"

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
