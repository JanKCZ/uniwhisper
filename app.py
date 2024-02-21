from flask import Flask, request, render_template
from openai import OpenAI
from flask import jsonify
import os


app = Flask(__name__)
apikey = os.environ['API_KEY']
client = OpenAI(api_key=apikey)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        audio_file = request.files['file']
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        text = transcript.text
        return render_template('index.html', text=text)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio_file = request.files['file']
    file_in_bytes = audio_file.read()
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=(audio_file.filename, file_in_bytes)
    )
    text = transcript.text
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
