from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze') 
    response = emotion_detector(text_to_analyze)
    return ""

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel
    '''

    return render_template('index.html')


if __name__ == "__main__":
    '''
    This function executes the flask app and deploys it on localhost:5000
    '''

    app.run(host="0.0.0.0", port=5000, debug=True)