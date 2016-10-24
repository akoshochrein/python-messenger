import mock
import pytest

from messenger import Bot


class MockBot(Bot):
    def _send(self, message_payload):
        return message_payload

    def handle_message(self, messaging_event):
        return messaging_event


class TestBotClass(object):
    mock_validation_token = 'mock-validation-token'
    mock_page_access_token = 'mock-validation-token'

    @pytest.fixture(scope='class', autouse=True)
    def bot_fixture(self):
        yield MockBot(self.mock_validation_token, self.mock_page_access_token)

    def test_bot_has_correct_validation_token(self, bot_fixture):
        assert self.mock_validation_token == bot_fixture.validation_token

    def test_bot_has_correct_page_access_token(self, bot_fixture):
        assert self.mock_page_access_token == bot_fixture.page_access_token

    def test_validation(self, bot_fixture):
        assert bot_fixture.token_is_valid(self.mock_validation_token)

    def test_message_gets_processed_by_handle_message(self, bot_fixture):
        bot_fixture.handle_message = mock.Mock()
        bot_fixture.process_message({'object': 'page', 'entry': [{'messaging': [{'message': 'test'}]}]})
        assert 1 == bot_fixture.handle_message.call_count
        assert {'message': 'test'} == bot_fixture.handle_message.call_args[0][0]

    def test_not_implemented(self, bot_fixture):
        with pytest.raises(NotImplementedError):
            bot_fixture.process_message({'object': 'page', 'entry': [{'messaging': [{'optin': 'test'}]}]})
