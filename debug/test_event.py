import json
from debug.event_data import fetch_event_data_list

test_input = {
    "Records": [{
        "body": json.dumps({
            'Type':             'Notification',
            'MessageId':        'c57284ca-2bbe-5176-9e75-dcdd50f5fcb7',
            'TopicArn':         fetch_event_data_list()["TEST"]["TOPIC_ARN"],
            'Message':          fetch_event_data_list()["TEST"]["MESSAGE"],
            'Timestamp':        '2020-10-31T14:47:39.557Z',
            'SignatureVersion': '1',
            'Signature':        'AokIcy4uyUsiL+MATB7aIjxzic+KEkyVCwGfkTuwElEVO8w1jW0w13LM+hIVxWSsQRTn/DITnNbnyR84X4CN8y6xlpxezFe1m5K9iHg/HVLaGTFTKx1ugHqAVKBufihwsz+VAzJOGZiBC2H1787C2HYjhO9bIsF/9vvb0ivjYgCQp0CY7SPK4mIoID2U6Pab5xcSbCroeeoAD2XoVOYFOZ/gR1mBDFb8ef6Q8wV9S/nZtYFaVmpwLOCP6LHqOXRGf1UUqTaBzEp+k7VU4Eu0MhGk6y74JqkQhYnD1ytUuX/4239wTtiqErkQq4QEtsFvwc+OxZi9Syb4hkY1PmN/sQ=="',
            'SigningCertURL':   'https://sns.eu-west-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem',
            'UnsubscribeURL':   'https://sns.eu-west-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-1:558711342920:development_ORDER_UPDATE_BAG_TYPE:bcd7ff0d-e1bb-4f75-a8ce-cd773778d90f',
        }),
        'attributes': {'ApproximateReceiveCount': '3354', 'SentTimestamp': '1604155659601', 'SenderId': 'AIDAISMY7JYY5F7RTT6AO', 'ApproximateFirstReceiveTimestamp': '1604155659601'},
        'messageAttributes': {},
        'md5OfBody': '18a2510ced7faa6d6462cbae5377d7f6',
        'eventSource': 'aws:sqs',
        'eventSourceARN': 'arn:aws:sqs:eu-west-1:558711342920:dev-warehouse-robot',
        'awsRegion': 'eu-west-1',
    }]
}


def fetch_test_input():
    print(fetch_event_data_list())
    return test_input
