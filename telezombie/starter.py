from tornado import gen, ioloop
from telezombie import api


class KelThuzad(api.TeleLich):

    def __init__(self, api_token):
        super(KelThuzad, self).__init__(api_token)

    @gen.coroutine
    def on_text(self, message):
        id_ = message.message_id
        chat = message.chat
        text = message.text
        # echo same text
        yield self.send_message(chat.id_, text, reply_to_message_id=id_)


@gen.coroutine
def forever():
    API_TOKEN = '231573402:AAH9Dwo7QONselTFxeLIAbN1ElvYPjNi1CE'
    lich = KelThuzad(API_TOKEN)

    yield lich.poll()


main_loop = ioloop.IOLoop.instance()
main_loop.run_sync(forever)