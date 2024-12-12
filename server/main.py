from flask import Flask, request, jsonify
import os
from flask_cors import CORS
import google.generativeai as gemini

app = Flask(__name__)
CORS(app)

# Initialize Google Gemini API
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set")
gemini.api_key = gemini_api_key
model = gemini.GenerativeModel("gemini-1.5-flash")

@app.route('/api/prompt', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        # Process the message using Google Gemini
        response = model.generate_content(message)
        if 'choices' in response and len(response['choices']) > 0:
            generated_message = response['choices'][0]['text']
        else:
            return jsonify({'error': 'No text generated'}), 500

        return jsonify({'message': generated_message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)