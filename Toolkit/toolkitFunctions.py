class ToolkitFunctions:
    def __init__(self, api):
        # Initialize toolkit functions with a toolkit connection instance
        self.api = api

    # Lambda functions to be used for virtual pet interactions
    def update_negative_emotions(
        self,
        emotional_entity,
        sadness_amount,
        fear_amount,
        anger_amount,
        disgust_amount,
    ):
        event = {
            "emotional_entity": emotional_entity,
            "sadness_amount": sadness_amount,
            "fear_amount": fear_amount,
            "anger_amount": anger_amount,
            "disgust_amount": disgust_amount,
        }
        return self.api.call_lambda_function("updateNegativeEmotions", event)

    def update_positive_emotions(
        self,
        emotional_entity,
        happiness_amount,
        surprise_amount,
    ):
        event = {
            "emotional_entity": emotional_entity,
            "happiness_amount": happiness_amount,
            "surprise_amount": surprise_amount,
        }
        return self.api.call_lambda_function("updatePositiveEmotions", event)
