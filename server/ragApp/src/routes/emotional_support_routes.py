from flask import Blueprint, request, jsonify
from src.controllers.emotional_support import EmotionalSupportController

emotional_support_bp = Blueprint('emotional_support', __name__)
controller = EmotionalSupportController()

@emotional_support_bp.route('/api/emotional_support', methods=['POST'])
def handle_emotional_support():
    return controller.handle_emotional_support_prompt()