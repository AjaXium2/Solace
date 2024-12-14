from flask import jsonify
import google.generativeai as genai

class AnxietyService:
    def __init__(self):
        genai.configure(api_key="AIzaSyBb3TWHeNnVbd5KQ-_UDuJkWpjgdfnSLT4")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return str(e)