import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)
    emotion_dict = json.loads(response.text)["emotionPredictions"][0]["emotion"]

    dict_to_return = {
        "anger_score": emotion_dict["anger"],
        "disgust_score": emotion_dict["disgust"],
        "fear_score": emotion_dict["fear"],
        "joy_score": emotion_dict["joy"],
        "sadness_score": emotion_dict["sadness"]
    }
    dominant_emotion = max(dict_to_return, key=dict_to_return.get).split("_")[0]
    dict_to_return["dominant_emotion"] = dominant_emotion
    
    return dict_to_return