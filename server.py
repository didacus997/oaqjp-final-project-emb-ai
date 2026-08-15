"""
    This server is the backend application for the Emotion Detector web page
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

"""This function is to declare the route /emotionDetection"""
@app.route("/emotionDetector")
def sent_emotion():
    """This function is to perform the action"""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    return f"For the given statement, the system response is \
    'anger': {result['anger']}, \
    'disgust': {result['disgust']}, \
    'fear': {result['fear']}, \
    'joy': {result['joy']} and \
    'sadness': {result['sadness']}. \
    The dominant emotion is <b>{result['dominant_emotion']}</b>."

@app.route("/")
def render_index_page():
    """This function is to go to the index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
