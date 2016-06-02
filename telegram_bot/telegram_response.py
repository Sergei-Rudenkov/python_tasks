import requests


class TelegramResponse(object):

    def __init__(self):
        self.botToken = "231573402:AAH9Dwo7QONselTFxeLIAbN1ElvYPjNi1CE"

    def getResponse(self):
        return requests.get(
            url='https://api.telegram.org/bot{0}/{1}'.format(self.botToken, "getUpdates")
        ).json()

    def getAllChatId(self):
        response = self.getResponse()
        return set([response['result'][n]["message"]["chat"]["id"] for n in range(len(response['result']))])

    def getLastChatId(self):
        response = self.getResponse()
        return response['result'][-1]["message"]["chat"]["id"]

    def getLastMessage(self, interlocutor_id):
        response = self.getResponse()
        returnList = [response['result'][n]['message']['text'] for n in range(len(response['result'])) if
               response['result'][n] == response['result'][-1] and response['result'][n]['message']['from'][
                   'id'] == interlocutor_id]
        return returnList[0]

    def getLastMessageId(self, interlocutor_id):
        response = self.getResponse()
        returnList = [response['result'][n]['message']['message_id'] for n in range(len(response['result'])) if
                response['result'][n] == response['result'][-1] and response['result'][n]['message']['from'][
                    'id'] == interlocutor_id]
        return returnList[0]

    def getUserLastNameById(self, interlocutor_id):
        response = self.getResponse()
        nameList = [response['result'][n]['message']['from']['last_name'] for n in range(len(response['result'])) if
               response['result'][n] == response['result'][-1] and response['result'][n]['message']['from'][
                   'id'] == interlocutor_id]
        return nameList[0]