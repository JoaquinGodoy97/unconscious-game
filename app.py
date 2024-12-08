import ffmpeg
from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return "No file part"
    file = request.files["file"]

    input_audio = BytesIO(file.read())
    output_audio = BytesIO();
    input_audio.seek(0)
    # recognizer = sr.Recognizer()
    
    try:

        process = (
            ffmpeg
            .input("pipe:0")
            .output("pipe:1", format="wav")
            .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True)
        )
        # Pass the WebM audio data and get WAV output
        output, _ = process.communicate(input=input_audio.read())
        output_audio.write(output)
        output_audio.seek(0)
        
        recognizer = sr.Recognizer()
        with sr.AudioFile(output_audio) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return "Speech recognition could not understand audio"
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An error occurred during audio processing: {e}"

if __name__ == '__main__':
    app.run(debug=True)
