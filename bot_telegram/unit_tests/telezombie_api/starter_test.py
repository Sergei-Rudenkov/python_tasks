import unittest

from mock import mock

import bot_telegram.starter
from bot_telegram.telezombie import types


class TestHelloApp(unittest.TestCase):
    def test_app(self):
        message = types.Message({'message_id': '1', 'text': 'Ў',
                                 'chat': {"id": 227071993, "first_name": "Sergei", "last_name": "Rudenkov",
                                          "type": "private"}, 'from': 343})

        zombie = bot_telegram.starter.KelThuzad('API_TOKEN', 'SO_WS_URL')
        zombie.on_text(message)
        with mock.patch.object(bot_telegram.starter.KelThuzad, 'send_message') as mock_zombie:
            mock_zombie.assert_called_with(227071993,
                                           """Sorry, I didn't find anything according to you request.
                                           Try again!""",
                                           1)


if __name__ == '__main__':
    unittest.main()
