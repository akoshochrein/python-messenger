import json
import requests

from messenger.const import *
from messenger.exceptions import InvalidMessageException


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

        if OBJECT_PAGE == data.get(MESSAGE_DATA_OBJECT):
            for page_entry in data.get(MESSAGE_DATA_ENTRY):
                for messaging_event in page_entry.get(PAGE_ENTRY_MESSAGING):
                    if messaging_event.get(EVENT_OPTIN):
                        self.handle_optin(messaging_event)
                    elif messaging_event.get(EVENT_MESSAGE):
                        self.handle_message(messaging_event)
                    elif messaging_event.get(EVENT_DELIVERY):
                        self.handle_delivery(messaging_event)
                    elif messaging_event.get(EVENT_POSTBACK):
                        self.handle_postback(messaging_event)
                    elif messaging_event.get(EVENT_READ):
                        self.handle_read(messaging_event)
                    elif messaging_event.get(EVENT_ACCOUNT_LINKING):
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
        message_payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': text
            }
        }
        self._send(message_payload)

    def send_text_message_with_attachment(self, recipient_id, text, attachment):
        message_payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': text,
                'attachment': attachment.to_dict()
            }
        }
        self._send(message_payload)

    def send_attachment(self, recipient_id, attachment):
        message_payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'attachment': attachment.to_dict()
            }
        }
        self._send(message_payload)

    def send_generic_template(self, recipient_id, template):
        message_payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'attachment': template.to_dict()
            }
        }
        self._send(message_payload)

    def send_sender_action(self, recipient_id, sender_action):
        message_payload = {
            'recipient': {
                'id': recipient_id
            },
            'sender_action': sender_action
        }
        self._send(message_payload)

    def send_quick_reply(self, recipient_id, quick_replies=None):
        message_payload = {
            'recipient': {
                'id': recipient_id
            },
            'quick_replies': [
                qr.to_dict() for qr in quick_replies
            ]
        }
        self._send(message_payload)
