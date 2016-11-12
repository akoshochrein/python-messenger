from messenger.models import QuickTextReply
from messenger.models.quick_replies import QUICK_REPLY_CONTENT_TYPE_TEXT


class TestQuickTextReply(object):
    mock_title = 'mock-title'
    mock_payload = 'mock-payload'

    def test_create(self):
        qtr = QuickTextReply(self.mock_title, self.mock_payload)

        assert self.mock_title == qtr.title
        assert self.mock_payload == qtr.payload

    def test_to_dict(self):
        qtr = QuickTextReply(self.mock_title, self.mock_payload)

        qtr_dict = qtr.to_dict()

        assert QUICK_REPLY_CONTENT_TYPE_TEXT == qtr_dict['content_type']
        assert self.mock_title == qtr_dict['title']
        assert self.mock_payload == qtr_dict['payload']
