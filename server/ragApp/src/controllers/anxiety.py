from flask import request, jsonify
from ..services.anxiety_service import AnxietyService

class AnxietyController:
    def __init__(self):
        self.service = AnxietyService()

    def handle_anxiety_prompt(self):
        data = request.get_json()
        message = data.get('message', '')
        response = self.service.generate_response(message)
        return jsonify({'message': response})