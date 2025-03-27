"""
Emotion Detection File 

This python script destablishes the logic and api response for emotion detection using user input in the form of text.
"""

import requests
import json

def emotion_detector(text_to_analyze):
    # info for request
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } } 

    # make the post request
    response = requests.post(URL, json=input_json, headers=header)

    # format response
    formatted_response = json.loads(response.text)

    # error handling and formatted response
    if response.status_code == 400:
        keys = formatted_response.keys()

        # return None for values if 400 code
        for key in keys:
            formatted_response[key] = None

        formatted_response['dominant_emotion'] = None
    # otherwise format repsponse for output
    else:
        emotions = (formatted_response['emotionPredictions'][0])['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        sadness_score = emotions['sadness']
        
        # get dom emotion via max of scores
        dominant_emotion = max(emotions, key=emotions.get)

        #format response
        display_response_format = {
                                'anger': anger_score,
                                'disgust': disgust_score,
                                'fear': fear_score,
                                'sadness': sadness_score,   
                                'dominant_emotion': dominant_emotion
                            }

    # return formatted response
    return display_response_format
