from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_dict = emotion_detector(text_to_analyze)

    anger_score = emotion_dict["anger"]
    disgust_score = emotion_dict["disgust"]
    fear_score = emotion_dict["fear"]
    joy_score = emotion_dict["joy"]
    sadness_score = emotion_dict["sadness"]
    dominant_emotion = emotion_dict["dominant_emotion"]

    string_to_return = (
        f"For the given statement, the system response is"
        "'anger': {anger_score}, "
        "'disgust': {disgust_score}, "
        "'fear': {fear_score}, "
        "'joy': {joy_score} and "
        "'sadness': {sadness_score}. "
        "The dominant emotion is {dominant_emotion}"
    )

    return string_to_return

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)