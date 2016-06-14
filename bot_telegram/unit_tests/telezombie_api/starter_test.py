import unittest

from mock import mock

import bot_telegram.starter
from bot_telegram.telezombie import types


class TestBotStaterApi(unittest.TestCase):
    def test_non_ascii_char_query(self):
        chat_id = 227071993
        text = 'Ў'
        message_id = 1
        message = types.Message({'message_id': message_id, 'text': text,
                                 'chat': {"id": chat_id, "first_name": "Sergei", "last_name": "Rudenkov",
                                          "type": "private"}, 'from': 343})
        zombie = bot_telegram.starter.KelThuzad('API_TOKEN', 'SO_WS_URL')
        with mock.patch.object(bot_telegram.starter.KelThuzad, 'send_message') as mock_zombie:
            zombie.on_text(message)
            mock_zombie.assert_called_with(chat_id,
                                           """Sorry, I didn't find anything according to you request. Try again!""",
                                           reply_to_message_id=message_id)

    def test_ascii_char_query(self):
        text = 'Hello-World'
        message_id = 1
        chat_id = 227071993
        message = types.Message({'message_id': message_id, 'text': text,
                                 'chat': {"id": chat_id, "first_name": "Sergei", "last_name": "Rudenkov",
                                          "type": "private"}, 'from': 343})
        zombie = bot_telegram.starter.KelThuzad('API_TOKEN', 'SO_WS_URL')
        with mock.patch.object(bot_telegram.starter.KelThuzad, 'perform_search') as mock_zombie:
            zombie.on_text(message)
            mock_zombie.assert_called_with(text, message_id, message.chat)

    def test_perform_search(self):
        text = 'Hello-World'
        message_id = 1
        chat_id = 227071993
        message = types.Message({'message_id': message_id, 'text': text,
                                 'chat': {"id": chat_id, "first_name": "Sergei", "last_name": "Rudenkov",
                                          "type": "private"}, 'from': 343})

        zombie = bot_telegram.starter.KelThuzad('API_TOKEN', 'SO_WS_URL')
        with mock.patch.object(bot_telegram.starter.KelThuzad, 'ws_get') as mock_urlopen:
            mock_urlopen.return_value = '{"message": "ok!"}'

            with mock.patch.object(bot_telegram.starter.KelThuzad, 'send_message') as mock_send_message:
                zombie.perform_search("hello", 1, message.chat)
                mock_send_message.assert_called_with(1, 2, message.chat)

if __name__ == '__main__':
    unittest.main()
