import random
from threading import Thread

import time

import telegram_bot.telegram_response
from telegram_bot.bot_response import BotResponse


def wait_response(chatId):
    bot_response = BotResponse()
    while True:
        time.sleep(10)
        bot_response.answer(random.choice(
            ["Cheer up!", "Chin up!", "Smile!", "It's not the end of the world.", "Worse things happen at sea.",
            "Look on the bright side........", "Every cloud(has a silver lining).", "Practice makes perfect.",
            "There are plenty more fish in the sea.", "Lighten up!", "There's no use crying over spilt milk."]),
            chatId)

client_response = telegram_bot.telegram_response.TelegramResponse()
chats = client_response.getAllChatId()
print(chats)
for chat_id in chats:
    d = Thread(target=wait_response, args=(chat_id,))
    d.setDaemon(False)
    d.start()



