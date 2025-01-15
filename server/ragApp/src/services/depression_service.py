from flask import jsonify
import google.generativeai as genai
import os

from decouple import config

# Lire les clés API depuis .env
GEMINI_API_KEY = config('GEMINI_API_KEY')
class DepressionService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text