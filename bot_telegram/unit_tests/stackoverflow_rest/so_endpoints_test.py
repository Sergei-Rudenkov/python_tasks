import unittest

from mock import mock

import bot_telegram.starter


class TestSoEndpoints(unittest.TestCase):

    def test_so_get(self):
        pass
    #     with mock.patch.object(bot_telegram.stackoverflow_rest.so_endpoints.StackOverflowHandler, 'fetch_so') as mock_urlopen:
    #         mock_urlopen.return_value = '{"message": "ok!"}'
    #
    #         so = bot_telegram.stackoverflow_rest.so_endpoints.StackOverflowHandler()
    #         with mock.patch.object(bot_telegram.stackoverflow_rest.so_endpoints.StackOverflowHandler, 'write') as my_mock:
    #             so.get("hello")
    #             my_mock.assert_called_with(1, 2)


if __name__ == '__main__':
    unittest.main()