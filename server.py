''' Executing this function initiates the application of emotion 
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """ Receives text from the HTML interface and runs
        emotion detection over it using emotion_detector().
        Outputs text specifying the 'score' for 5 different
        emotions as well as the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_dict = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_dict["dominant_emotion"]

    if dominant_emotion is None:
        string_to_return = "Invalid text! Please try again!"
    else:
        string_list = [f"'{emotion}': {score}" for (emotion, score) in emotion_dict.items() if emotion != "dominant_emotion"]
        string_top = string_list[:-1]
        string_last_element = string_list[-1]
        emotions_score_string = f"{', '.join(string_top)}, and {string_last_element}"
        string_to_return = f"For the given statement, the system response is {emotions_score_string}.\
                             The dominant emotion is {dominant_emotion}."

    return string_to_return

@app.route("/")
def render_index_page():
    ''' Initiates the rendering of the main application page over the Flask channel'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
