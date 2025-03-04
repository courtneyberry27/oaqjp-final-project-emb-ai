import requests
import json

def emotion_detector(text_to_analyze):
    # info for request
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } } 

    # make the post request
    response = requests.post(URL, json=input_json, headers=header)
    formatted_response = json.loads(response.text)

    emotions = (formatted_response['emotionPredictions'][0])['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    sadness_score = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)
    display_response_format = {
                            'anger': anger_score,
                            'disgust': disgust_score,
                            'fear': fear_score,
                            'sadness': sadness_score,   
                            'dominant_emotion': dominant_emotion
                        }

    # return formatted response
    print(display_response_format)
    return display_response_format
