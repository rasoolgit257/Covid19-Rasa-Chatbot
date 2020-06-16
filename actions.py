# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('printing hello world via actions')

        dispatcher.utter_message(text="Hello World! from actions")

        return []

class Actionsearchresturant(Action):

    def name(self) -> Text:
        return "action_search_resturant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities =tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'hotel':
                name = e['value']

            if name == 'indian':
                message = "indian1,indian2,indian3"

            if name == 'china':
                message = "china1,china2,china3"


        dispatcher.utter_message(text="message")

        return []


class Actioncoronatracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()
        entities =tracker.latest_message['entities']
        print(entities)

        state=None

        for e in entities:
            if e['entity'] == 'state':
                state = e['value']

        message =  'enter vaild name'

        for data in response['statewise']:
            if data['state'] == state.title():
                print(data)
                message='Active: '+ data['active']+'confirmed: '+ data['confirmed']
        print(message)

        dispatcher.utter_message(text=message)

        return []
