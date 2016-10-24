import json
import requests

from .exceptions import InvalidMessageException


class Bot(object):

    def __init__(self, validation_token, page_access_token):
        self.validation_token = validation_token
        self.page_access_token = page_access_token

    def token_is_valid(self, validation_token):
        return self.validation_token == validation_token

    def _message_is_valid(self, message):
        return True

    def process_message(self, data):
        if not self._message_is_valid(data):
            raise InvalidMessageException

        if 'page' == data.get('object'):
            for page_entry in data.get('entry'):

                for messaging_event in page_entry.get('messaging'):
                    if messaging_event.get('optin'):
                        self.handle_optin(messaging_event)
                    elif messaging_event.get('message'):
                        self.handle_message(messaging_event)
                    elif messaging_event.get('delivery'):
                        self.handle_delivery(messaging_event)
                    elif messaging_event.get('postback'):
                        self.handle_postback(messaging_event)
                    elif messaging_event.get('read'):
                        self.handle_read(messaging_event)
                    elif messaging_event.get('account_linking'):
                        self.handle_account_linking(messaging_event)
                    else:
                        pass

    def handle_optin(self, messaging_event):
        raise NotImplementedError

    def handle_message(self, messaging_event):
        raise NotImplementedError

    def handle_delivery(self, messaging_event):
        raise NotImplementedError

    def handle_postback(self, messaging_event):
        raise NotImplementedError

    def handle_read(self, messaging_event):
        raise NotImplementedError

    def handle_account_linking(self, messaging_event):
        raise NotImplementedError

    def _send(self, message_payload):
        requests.post(
            'https://graph.facebook.com/v2.6/me/messages?access_token={access_token}'.format(
                access_token=self.page_access_token
            ),
            data=json.dumps(message_payload),
            headers={'content-type': 'application/json'}
        )

    def send_text_message(self, recipient_id, text):
        message_data = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': text
            }
        }
        self._send(message_data)
