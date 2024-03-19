# Class that modifies emotions, using a Lambda API
class EmotionModifier:
    def __init__(self, api):
        # Initialize EmotionModifier with a Lambda API instance
        self.api = api

    # Method to update happiness
    def update_happiness(self, emotional_entity, happiness_amount):
        # Build the API event for updating happiness
        event = self._build_event(
            "updateHappiness", emotional_entity, happiness_amount=happiness_amount
        )
        # Call the Lambda function to update happiness and return the result
        return self.api.call_lambda_function(event)

    # Method to update negative emotions
    def update_negative_emotions(
        self,
        emotional_entity,
        sadness_amount,
        fear_amount,
        anger_amount,
        disgust_amount,
    ):
        event = self._build_event(
            "updateNegativeEmotions",
            emotional_entity,
            sadness_amount=sadness_amount,
            fear_amount=fear_amount,
            anger_amount=anger_amount,
            disgust_amount=disgust_amount,
        )
        return self.api.call_lambda_function(event)

    # Private method to build the API event
    def _build_event(self, function_to_call, emotional_entity, **kwargs):
        # Construct the API event dictionary with the specified function and emotional entity
        event = {
            "function_to_call": function_to_call,
            "emotional_entity": emotional_entity,
        }
        # Update the event dictionary with additional keyword arguments
        event.update(kwargs)
        return event
