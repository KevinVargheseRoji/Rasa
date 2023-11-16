# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
import asyncio
import tracemalloc
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class MyCustomAction(Action):
    async def run(self, dispatcher, tracker, domain):
        # Enable tracemalloc
        tracemalloc.start()

        # Use asyncio.gather() to create a future and pass it to asyncio.wait()
        futures = {asyncio.gather(self.async_function(), self.async_function())}
        await asyncio.wait(futures)

        # Perform other actions if needed
        dispatcher.utter_message("Custom action completed.")

        # Return any events that should be triggered
        return [SlotSet("custom_slot", "value")]

    async def async_function(self):
        # Some asynchronous code
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(MyCustomAction().run(None, None, None))


