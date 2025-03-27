"""
Emotion Detection Server File

This python script defines a flask server for emotion detection using 
user input in the form of text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector", methods=['GET'], strict_slashes=False)

def format_response():
    """Analyze text for emotions
    and return string with emotion scores and the dominant emotion overall."""
    # get input from app
    input_text = request.args.get('textToAnalyze')
    # use emotion detector function with input
    response = emotion_detector(input_text)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
            f"For the given statement, the system response is 'anger': {response['anger']} "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")

def home():
    """render index.html file."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
