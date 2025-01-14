from flask import jsonify
import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyDaUliNYw3pJMmw5ePWlrAOzt7tF_vfg58')

class EmotionalSupportService:
    def __init__(self):

        api_key = os.getenv(GEMINI_API_KEY)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_emotional_support_response(self, message):
        response = self.model.generate_content(message)
        return response.text