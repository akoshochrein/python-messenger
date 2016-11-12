import pytest

from messenger.models import QuickTextAndImageReply, QuickTextReply
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

    def test_create_failed_title(self):
        with pytest.raises(AssertionError):
            QuickTextReply('#' * 21, self.mock_payload)

    def test_create_failed_payload(self):
        with pytest.raises(AssertionError):
            QuickTextReply(self.mock_title, '#' * 1001)


class TestQuickTextAndImageReply(object):
    mock_title = 'mock-title'
    mock_image_url = 'mock://image-url'
    mock_payload = 'mock-payload'

    def test_create(self):
        qtair = QuickTextAndImageReply(self.mock_title, self.mock_image_url, self.mock_payload)

        assert self.mock_title == qtair.title
        assert self.mock_image_url == qtair.image_url
        assert self.mock_payload == qtair.payload

    def test_to_dict(self):
        qtair = QuickTextAndImageReply(self.mock_title, self.mock_image_url, self.mock_payload)

        qtair_dict = qtair.to_dict()

        assert QUICK_REPLY_CONTENT_TYPE_TEXT == qtair_dict['content_type']
        assert self.mock_title == qtair_dict['title']
        assert self.mock_image_url == qtair_dict['image_url']
        assert self.mock_payload == qtair_dict['payload']

    def test_create_failed_title(self):
        with pytest.raises(AssertionError):
            QuickTextAndImageReply('#' * 21, self.mock_image_url, self.mock_payload)

    def test_create_failed_payload(self):
        with pytest.raises(AssertionError):
            QuickTextAndImageReply(self.mock_title, self.mock_image_url, '#' * 1001)
