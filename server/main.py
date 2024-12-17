from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from ragApp.src.services.main_service import MainService
from apis.voice import generateAudio
import io

app = Flask(__name__, static_url_path='/', static_folder='audios')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

main_service = MainService()

@app.route('/api/prompt', methods=['POST'])
def handle_prompt():
    try:
        data = request.get_json()
        message = data.get('message', '')
        prompt_type = data.get('type', 'general')
        response_text = main_service.generate_response(message, prompt_type)
        return jsonify({'message': response_text})
    except Exception as e:
        app.logger.error(f"Error processing message: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate_audio', methods=['POST'])
def generate_audio():
    try:
        data = request.get_json()
        message = data.get('text', '')
        audio_bytes = generateAudio(message)
        return send_file(io.BytesIO(audio_bytes), mimetype='audio/wav', as_attachment=False, download_name='audio.wav')
    except Exception as e:
        app.logger.error(f"Error generating audio: {str(e)}")
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(port=5001)