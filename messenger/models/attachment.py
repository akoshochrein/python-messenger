from messenger.const import ATTACHMENT_TYPE_IMAGE, ATTACHMENT_TYPE_AUDIO, ATTACHMENT_TYPE_VIDEO, ATTACHMENT_TYPE_FILE

ATTACHMENT_TYPES = [ATTACHMENT_TYPE_IMAGE, ATTACHMENT_TYPE_AUDIO, ATTACHMENT_TYPE_VIDEO, ATTACHMENT_TYPE_FILE]


class Attachment(object):

    def __init__(self, typ, url):
        assert typ in ATTACHMENT_TYPES, 'Invalid attachment type'
        self.typ = typ
        self.url = url

    def to_dict(self):
        return {
            "type": self.typ,
            "payload": {
                "url": self.url
            }
        }
