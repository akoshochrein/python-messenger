
QUICK_REPLY_CONTENT_TYPE_TEXT = 'text'


class QuickTextReply(object):

    def __init__(self, title, payload):
        self.title = title
        self.payload = payload

    def to_dict(self):
        return {
            'content_type': QUICK_REPLY_CONTENT_TYPE_TEXT,
            'title': self.title,
            'payload': self.payload
        }
