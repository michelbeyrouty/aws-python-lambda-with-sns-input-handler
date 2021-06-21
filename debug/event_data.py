event_data_list = {
    "TEST": {
        "MESSAGE":   '{"body":"Hello World !!!"}',
        "TOPIC_ARN": 'arn:aws:sns:eu-west-1:558711342920:development_TEST',
    }
}


def fetch_event_data_list():
    return event_data_list
