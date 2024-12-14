from flask import jsonify
import google.generativeai as genai

class MainService:
    def __init__(self):
        genai.configure(api_key="AIzaSyBb3TWHeNnVbd5KQ-_UDuJkWpjgdfnSLT4")
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