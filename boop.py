from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Create a directory to store the audio files
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle audio uploads (POST request)
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    file_name = os.path.join('uploads', 'audio_chunk.webm')

    with open(file_name, 'ab') as f:
        f.write(audio_file.read())

    return jsonify({'message': 'Audio chunk received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
