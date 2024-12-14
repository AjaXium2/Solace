from flask import jsonify
import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

class MainService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, message, prompt_type):
        if prompt_type == 'depression':
            message = f"Provide support for someone feeling depressed: {message}"
        elif prompt_type == 'anxiety':
            message = f"Provide support for someone feeling anxious: {message}"
        elif prompt_type == 'emotional_support':
            message = f"Provide emotional support: {message}"
        response = self.model.generate_content(message)
        return response.text