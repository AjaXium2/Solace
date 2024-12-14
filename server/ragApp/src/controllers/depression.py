from flask import request, jsonify
from ..services.depression_service import DepressionService

class DepressionController:
    def __init__(self):
        self.depression_service = DepressionService()

    def handle_depression_prompt(self):
        data = request.get_json()
        message = data.get('message', '')
        response = self.depression_service.generate_response(message)
        return jsonify({'message': response})