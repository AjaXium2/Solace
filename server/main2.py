from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

genai.configure(api_key="AIzaSyAfm_3uBqRdN86XLa7weHilCJNlMmj3NXs")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/api/prompt', methods=['POST'])
def handle_prompt():
    try:
        data = request.get_json()
        message = data.get('message', '')
        response = model.generate_content(message)
        return jsonify({'message': response.text})
    except Exception as e:
        app.logger.error(f"Error processing message: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)