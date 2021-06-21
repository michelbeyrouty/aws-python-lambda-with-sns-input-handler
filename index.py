################################################################
#               Washmen payment robot                          #
#                                                              #
# Author: Michel el beyrouthy [michel.beyrouty@getwashmen.com] #
#         "Code is more often read than written."              #
################################################################
import json
from core.lambda_handler import LambdaHandler

def lambda_handler(event, context):

    Records = event["Records"]

    for record in Records:
        input_event = json.loads(record["body"])
        lambda_handler = LambdaHandler()
        lambda_handler.handle_event(input_event)
