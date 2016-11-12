
QUICK_REPLY_CONTENT_TYPE_TEXT = 'text'
QUICK_REPLY_CONTENT_TYPE_LOCATION = 'location'


class QuickTextReply(object):

    def __init__(self, title, payload):
        assert len(title) < 21, 'Title limit of 20 chars reached'
        assert len(payload) < 1001, 'Payload limit of 1000 chars reached'
        self.title = title
        self.payload = payload

    def to_dict(self):
        return {
            'content_type': QUICK_REPLY_CONTENT_TYPE_TEXT,
            'title': self.title,
            'payload': self.payload
        }


class QuickTextAndImageReply(object):

    def __init__(self, title, image_url, payload):
        assert len(title) < 21, 'Title limit of 20 chars reached'
        assert len(payload) < 1001, 'Payload limit of 1000 chars reached'
        self.title = title
        self.image_url = image_url
        self.payload = payload

    def to_dict(self):
        return {
            'content_type': QUICK_REPLY_CONTENT_TYPE_TEXT,
            'title': self.title,
            'image_url': self.image_url,
            'payload': self.payload
        }


class QuickLocationReply(object):

    def to_dict(self):
        return {
            'content_type': QUICK_REPLY_CONTENT_TYPE_LOCATION
        }
