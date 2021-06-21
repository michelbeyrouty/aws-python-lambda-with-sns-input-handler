# Used to run the lambda locally and test it
# TODO: move to debug folder

import json
from debug.test_event import fetch_test_input
from core.lambda_handler import LambdaHandler


def lambda_handler(event, context):

    Records = event["Records"]

    for record in Records:
        input_event = json.loads(record["body"])
        lambda_handler = LambdaHandler()
        lambda_handler.handle_event(input_event)


if __name__ == "__main__":
    event = fetch_test_input()
    lambda_handler(event, {})
