from flask import jsonify
import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyDaUliNYw3pJMmw5ePWlrAOzt7tF_vfg58')

class AnxietyService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return str(e)