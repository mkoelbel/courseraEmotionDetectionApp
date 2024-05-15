from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_dict = emotion_detector(text_to_analyze)

    if emotion_dict["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger_score = emotion_dict["anger_score"]
    disgust_score = emotion_dict["disgust_score"]
    fear_score = emotion_dict["fear_score"]
    joy_score = emotion_dict["joy_score"]
    sadness_score = emotion_dict["sadness_score"]
    dominant_emotion = emotion_dict["dominant_emotion"]

    string_to_return = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return string_to_return

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)