from flask import Blueprint, request, jsonify
from ..controllers.depression import DepressionController

depression_bp = Blueprint('depression', __name__)
controller = DepressionController()

@depression_bp.route('/api/depression/prompt', methods=['POST'])
def handle_depression_prompt():
    return controller.handle_depression_prompt()