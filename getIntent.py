# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:32:39 2019

@author: NSQ
"""
#https://stackoverflow.com/questions/55694596/dialogflow-api-access-follow-up-intent-in-python
import dialogflow
import json
from google.api_core.exceptions import InvalidArgument
from google.oauth2 import service_account

dialogflow_key = json.load(open(r'credential.json'))
credentials = (service_account.Credentials.from_service_account_info(dialogflow_key))
session_client = dialogflow.SessionsClient(credentials=credentials)


DIALOGFLOW_LANGUAGE_CODE = 'th'
DIALOGFLOW_PROJECT_ID = 'test-agent-wabqqi'
SESSION_ID = 'testuserid'
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

text_to_be_analyzed = ["ดีจ้า"]


for text in text_to_be_analyzed:
    text_input = dialogflow.types.TextInput(
        text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))

# =============================================================================
# text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
# query_input = dialogflow.types.QueryInput(text=text_input)
# try:
#     response = session_client.detect_intent(session=session, query_input=query_input)
# except InvalidArgument:
#     raise
# 
# print("Query text:", response.query_result.query_text)
# print("Detected intent:", response.query_result.intent.display_name)
# print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# print("Fulfillment text:", response.query_result.fulfillment_text)
# =============================================================================
