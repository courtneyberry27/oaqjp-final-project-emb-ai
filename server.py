from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector", methods=['GET'], strict_slashes=False)

def format_response():
    input_text = request.args.get('textToAnalyze')
    response = emotion_detector(input_text)

    return (
        f"For the given statement, the system response is 'anger': {response['anger']} "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
@app.route("/")

# need port to be localhost:5000
def home():
    return "Welcome to the Emotion Detection API!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)