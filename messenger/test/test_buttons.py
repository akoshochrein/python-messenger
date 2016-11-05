import pytest

from messenger.models import CallButton, PostbackButton, ShareButton, UrlButton
from messenger.models.button import BUTTON_TYPE_URL, BUTTON_TYPE_POSTBACK, BUTTON_TYPE_PHONE_NUMBER, BUTTON_TYPE_SHARE


class TestUrlButton(object):
    mock_title = 'mock-title'
    mock_url = 'test://mock-url'

    def test_create_success(self):
        button = UrlButton(self.mock_title, self.mock_url)

        assert self.mock_title == button.title
        assert self.mock_url == button.url

    def test_to_dict_success(self):
        button = UrlButton(self.mock_title, self.mock_url)

        button_dict = button.to_dict()

        assert BUTTON_TYPE_URL == button_dict['type']
        assert self.mock_title == button_dict['title']
        assert self.mock_url == button_dict['url']

    def test_create_failed_title_limit(self):
        with pytest.raises(AssertionError):
            UrlButton('#' * 21, self.mock_url)


class TestPostbackButton(object):
    mock_title = 'mock-title'
    mock_payload = 'mock-payload'

    def test_create_success(self):
        button = PostbackButton(self.mock_title, self.mock_payload)

        assert self.mock_title == button.title
        assert self.mock_payload == button.payload

    def test_to_dict_success(self):
        button = PostbackButton(self.mock_title, self.mock_payload)

        button_dict = button.to_dict()

        assert BUTTON_TYPE_POSTBACK == button_dict['type']
        assert self.mock_title == button_dict['title']
        assert self.mock_payload == button_dict['payload']

    def test_create_failed_title_limit(self):
        with pytest.raises(AssertionError):
            PostbackButton('#' * 21, self.mock_payload)

    def test_create_failed_payload_limit(self):
        with pytest.raises(AssertionError):
            PostbackButton(self.mock_title, '#' * 1001)


class TestCallButton(object):
    mock_title = 'mock-title'
    mock_phone_number = '+1234567890'

    def test_create_success(self):
        button = CallButton(self.mock_title, self.mock_phone_number)

        assert self.mock_title == button.title
        assert self.mock_phone_number == button.phone_number

    def test_to_dict_success(self):
        button = CallButton(self.mock_title, self.mock_phone_number)

        button_dict = button.to_dict()

        assert BUTTON_TYPE_PHONE_NUMBER == button_dict['type']
        assert self.mock_title == button_dict['title']
        assert self.mock_phone_number == button_dict['payload']

    def test_create_failed_title_limit(self):
        with pytest.raises(AssertionError):
            CallButton('#' * 21, self.mock_phone_number)

    def test_create_failed_phone_number(self):
        with pytest.raises(AssertionError):
            CallButton(self.mock_title, 'not-a-phone-number')


class TestShareButton(object):

    def test_to_dict_success(self):
        button = ShareButton()

        button_dict = button.to_dict()

        assert BUTTON_TYPE_SHARE == button_dict['type']
