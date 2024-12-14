from flask import request, jsonify
from src.services.emotional_support_service import EmotionalSupportService

class EmotionalSupportController:
    def __init__(self):
        self.service = EmotionalSupportService()

    def handle_emotional_support_prompt(self):
        data = request.get_json()
        message = data.get('message', '')
        response = self.service.generate_response(message)
        return jsonify({'message': response})