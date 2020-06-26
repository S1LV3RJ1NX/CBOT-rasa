# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import stackconfig as cfg
from stackapi import StackAPI

KEY = cfg.stack["key"]
SITE = StackAPI('stackoverflow', key=KEY)

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_get_stack_query"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         print(domain)
#         dispatcher.utter_message(text="from stack")
#
#         return []

class StackOverFlowForm(FormAction):
    """Custom action to get answers to user queries on stack overflow"""

    def name(self) -> Text:
        return "stack_overflow_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots the form has to fill"""
        return ["stack_query"]

    def slot_mappings(self):
        return {
            "stack_query": [
                self.from_entity(entity="stack_query"),
                self.from_text(intent=None)
            ]
        }

    # def validate_query(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any]
    # ) -> Dict[Text, Any]:
    #     """Validate User Query"""
    #
    #     if value:
    #         return [SlotSet("stack_query", value)]
    #     else:
    #         dispatcher.utter_message(template="utter_wrong_query")
    #         return [SlotSet("stack_query", None)]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict]:
        """Define what form has to do after all slots have been filled"""
        title = tracker.get_slot("stack_query")
        # dispatcher.utter_message("Please wait fecting top 3 responses..!!")
        questions = SITE.fetch('similar', order='desc', sort='relevance', tagged='c', title=title)
        if questions['items']:
            dispatcher.utter_message("\nHere are your top 3 stack overflow suggestions:\n")
            for i in range(3):
                result = "Title: "+questions['items'][i]['title']+"\nLink: "+questions['items'][i]['link']+"\n"
                dispatcher.utter_message(result)
        else:
            dispatcher.utter_message("\n Sorry!! No relavant results found!!")
        return [SlotSet("stack_query", None)]
