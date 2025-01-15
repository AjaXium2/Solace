from flask import jsonify
import os
import google.generativeai as genai

from decouple import config

# Lire les clés API depuis .env
GEMINI_API_KEY = config('GEMINI_API_KEY')
class EmotionalSupportService:
    def __init__(self):

        api_key = os.getenv(GEMINI_API_KEY)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_emotional_support_response(self, message):
        response = self.model.generate_content(message)
        return response.text