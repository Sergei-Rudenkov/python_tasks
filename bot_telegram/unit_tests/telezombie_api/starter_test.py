import unittest
import mock as mock
import sys

import bot_telegram.starter
from bot_telegram.telezombie import types


class TestHelloApp(unittest.TestCase):
    @mock.patch.object(sys.modules['bot_telegram.telezombie'], 'KelThuzad')
    def test_app(self, mock_zombie):
        chat = types.Chat
        chat.id_ = 100
        message = types.Message({'message_id': '1', 'text': 'Ў', 'chat': chat})

        zombie = bot_telegram.starter.KelThuzad('API_TOKEN', 'SO_WS_URL')
        zombie.on_text(message)

        mock_zombie.send_message.assert_called_with(100,
                                             "Sorry, I didn't find anything according to you request. Try again!",
                                                    1)


if __name__ == '__main__':
    unittest.main()