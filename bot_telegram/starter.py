from tornado import gen, httpclient, ioloop
import json

from bot_telegram.telezombie import api


class KelThuzad(api.TeleLich):
    def __init__(self, api_token, ws_url):
        super().__init__(api_token)
        self.ws_url = ws_url

    @gen.coroutine
    def on_text(self, message):
        """
        User message controller
        """
        id_ = message.message_id
        chat = message.chat
        text = message.text.strip().replace(" ", "-").replace("[()&?]", "")
        if not self.is_ascii(text):
            yield self.send_message(chat.id_, "Sorry, I didn't find anything according to you request. Try again!",
                                    reply_to_message_id=id_)
        else:
            yield self.perform_search(text, id_, chat)

    @gen.coroutine
    def perform_search(self, text, id, chat):
        """
        Text handler fetch data from webserver
        """
        bot_response = yield self.ws_get(''.join([self.ws_url, text]))
        bot_response = json.loads(bot_response)
        if bot_response['links']:
            bot_response = bot_response['links'][0]
        else:
            bot_response = "Sorry, I didn't find anything according to you request. Try again!"
        yield self.send_message(chat.id_, bot_response, reply_to_message_id=id)

    @gen.coroutine
    def ws_get(self, url):
        """
        Fetch json from webserver by API:
        {host}:{port}/search/{pattern}
        """
        link = httpclient.AsyncHTTPClient()
        request = httpclient.HTTPRequest(url)
        response = yield link.fetch(request)
        data = response.body.decode('utf-8')
        return data

    def is_ascii(self, s):
        """
        Check if text sent by user is ascii
        """
        return s.encode("ascii", "ignore").decode("ascii") == s


@gen.coroutine
def forever():
    API_TOKEN = '231573402:AAH9Dwo7QONselTFxeLIAbN1ElvYPjNi1CE'
    SO_WS_URL = 'http://localhost:8888/search/'
    lich = KelThuzad(API_TOKEN, SO_WS_URL)
    yield lich.poll()

def main():
    main_loop = ioloop.IOLoop.instance()
    main_loop.run_sync(forever)

if __name__ == "__main__":
    main()