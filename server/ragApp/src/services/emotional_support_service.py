from flask import jsonify
import google.generativeai as genai

class EmotionalSupportService:
    def __init__(self):
        genai.configure(api_key="AIzaSyBb3TWHeNnVbd5KQ-_UDuJkWpjgdfnSLT4")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_emotional_support_response(self, message):
        response = self.model.generate_content(message)
        return response.text