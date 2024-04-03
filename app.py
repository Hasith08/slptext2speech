from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        text = request.form['text']
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3")  # On Windows
        # For Linux/Mac use:
        # os.system("xdg-open output.mp3")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
