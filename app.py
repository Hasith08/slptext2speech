from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os
from time import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', audio=False)

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        text = request.form['text']
        tts = gTTS(text=text, lang='en')
        timestamp = int(time())  # Get current timestamp
        filename = f"output_{timestamp}.mp3"  # Generate unique filename
        tts.save(f"static/{filename}")
        return render_template('index.html', audio=True, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)
