import requests
import json


# HTTP connection to AWS lambda API emotional modifier
class LambdaAPI:
    # Lambda API URL
    url_api_gateway = "https://sgzan1udv6.execute-api.us-east-2.amazonaws.com/emotionModifier/emotionModifierAPI"

    # Method that makes the call to the API Lambda function
    def call_lambda_function(self, event):
        try:
            response = requests.post(self.url_api_gateway, json=event)
            return self._process_response(response)
        except requests.exceptions.RequestException as e:
            return "Connection error: " + str(e)

    # Private method to process the API response
    def _process_response(self, response):
        if response.status_code == 200:
            lambda_response = json.loads(response.text)
            return lambda_response.get("body")
        else:
            return "Error calling Lambda function. Status code: " + str(
                response.status_code
            )
