import requests
import json


class ToolkitConnection:
    # Lambda toolkit URL
    base_url_toolkit = (
        "https://sgzan1udv6.execute-api.us-east-2.amazonaws.com/emotionModifier"
    )

    # Method that makes the call to the toolkit Lambda function
    def call_lambda_function(self, function_path, event):
        url = f"{self.base_url_toolkit}/{function_path}"
        try:
            response = requests.post(url, json=event)
            return self._process_response(response)
        except requests.exceptions.RequestException as e:
            return "Connection error: " + str(e)

    # Private method to process the toolkit response
    def _process_response(self, response):
        if response.status_code == 200:
            lambda_response = json.loads(response.text)
            return lambda_response.get("body")
        else:
            return "Error calling Lambda function. Status code: " + str(
                response.status_code
            )
