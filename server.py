'''Flask server for emotion detection'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    '''function to detect emotion'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle blank/invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel
    '''

    return render_template('index.html')


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
