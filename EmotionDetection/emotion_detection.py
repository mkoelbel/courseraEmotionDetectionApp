import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        dict_to_return = {
            "anger_score": None,
            "disgust_score": None,
            "fear_score": None,
            "joy_score": None,
            "sadness_score": None,
            "dominant_emotion": None
        }
    else:
        emotion_dict = json.loads(response.text)["emotionPredictions"][0]["emotion"]
        dict_to_return = emotion_dict
        dict_to_return["dominant_emotion"] = max(emotion_dict, key=emotion_dict.get)
    
    return dict_to_return