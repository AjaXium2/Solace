from flask import Blueprint, request, jsonify
from ..controllers.anxiety import AnxietyController

anxiety_routes = Blueprint('anxiety_routes', __name__)
controller = AnxietyController()

@anxiety_routes.route('/api/anxiety', methods=['POST'])
def handle_anxiety():
    return controller.handle_anxiety_prompt()