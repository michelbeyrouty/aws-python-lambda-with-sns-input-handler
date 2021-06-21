import json
import os
from core import routes


class LambdaHandler:

    def handle_event(self, event):
        sns_topic = self.get_sns_topic(event["TopicArn"])
        input_data = self.get_input_data(event["Message"])
        self.log_event(sns_topic, input_data)
        self.call_target_controller(sns_topic, input_data)

    def get_sns_topic(self, topic_arn):
        sns_topic_with_enviroment = topic_arn.split(":")[5]
        self.validate_enviroment(sns_topic_with_enviroment)
        return sns_topic_with_enviroment.split("_", 1)[1]

    def get_input_data(self, message):
        message_data = json.loads(message)
        return (message_data)

    def call_target_controller(self, sns_topic, input_data):
        target_controller = routes.fetch_controller(sns_topic)
        target_controller.process_data(input_data)

    def validate_enviroment(self, sns_topic_with_enviroment):
        system_enviroment = os.getenv('PYTHON_ENV')
        sns_enviroment = sns_topic_with_enviroment.split("_")[0]
        if not sns_enviroment == system_enviroment:
            raise TypeError("Wrong enviroment")

    def log_event(self, sns_topic, input_data):
        log_message = "snsTopic: " + sns_topic + "\ninputData:\n  "

        for variable in input_data.keys():
            log_message = log_message + variable + \
                ": " + input_data[variable] + "\n  "

        print(log_message)
