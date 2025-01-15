from flask import jsonify
import google.generativeai as genai
import os

from decouple import config

# Lire les clés API depuis .env
GEMINI_API_KEY = config('GEMINI_API_KEY')

class MainService:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("API key is missing. Set the GOOGLE_API_KEY environment variable.")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
                                                        
    def generate_response(self, message, prompt_type, max_characters=2000):
        if prompt_type == 'depression':
            message = f"Depression related prompt: {message}"
        elif prompt_type == 'anxiety':
            message = f"Anxiety related prompt: {message}"
        elif prompt_type == 'emotional_support':
            message = f"Emotional support related prompt: {message}"
            
        prompt = f"Generate a response with a maximum of {max_characters} characters: {message}"
        response = self.model.generate_content(prompt)
        return response.text
