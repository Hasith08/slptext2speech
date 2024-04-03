from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', audio=False)

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        text = request.form['text']
        tts = gTTS(text=text, lang='en')
        tts.save("static/output.mp3")
        return render_template('index.html', audio=True)

if __name__ == '__main__':
    app.run(debug=True)
