import requests


class BotResponse(object):

    def __init__(self):
        self.botToken = "231573402:AAH9Dwo7QONselTFxeLIAbN1ElvYPjNi1CE"

    def answer(self, message, chatId):
        method = "sendMessage"
        requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(self.botToken, method),
            data={'chat_id': chatId, 'text': message}
        ).json()