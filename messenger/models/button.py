

BUTTON_TYPE_URL = 'web_url'
BUTTON_TYPE_POSTBACK = 'postback'
BUTTON_TYPE_PHONE_NUMBER = 'phone_number'
BUTTON_TYPE_SHARE = 'element_share'


class UrlButton(object):

    def __init__(self, title, url):
        assert len(title) < 21, 'Title limit of 20 chars reached'
        self.title = title
        self.url = url

    def to_dict(self):
        return {
            'type': BUTTON_TYPE_URL,
            'url': self.url,
            'title': self.title
        }


class PostbackButton(object):

    def __init__(self, title, payload):
        assert len(title) < 21, 'Title limit of 20 chars reached'
        assert len(payload) < 1001, 'Payload limit of 1000 chars reached'
        self.title = title
        self.payload = payload

    def to_dict(self):
        return {
            'type': BUTTON_TYPE_POSTBACK,
            'title': self.title,
            'payload': self.payload
        }


class CallButton(object):

    def __init__(self, title, phone_number):
        assert len(title) < 21, 'Title limit of 20 chars reached'
        assert '+' == phone_number[0], 'Phone number must start with a + sign'
        self.title = title
        self.phone_number = phone_number

    def to_dict(self):
        return {
            'type': BUTTON_TYPE_PHONE_NUMBER,
            'title': self.title,
            'payload': self.phone_number
        }


class ShareButton(object):

    def to_dict(self):
        return {
            'type': BUTTON_TYPE_SHARE
        }
