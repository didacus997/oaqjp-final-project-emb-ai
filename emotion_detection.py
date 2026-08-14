import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = header)  
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion'] 
    sorted_dict = dict(sorted(emotion_dict.items(), key = lambda couple: couple[1], reverse=True))
    emotion_dict['dominant_emotion'] = next(iter(sorted_dict))
    return emotion_dict