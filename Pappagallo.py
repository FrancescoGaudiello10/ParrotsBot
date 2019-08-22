import telepot
from config import TOKEN
import sys, time

website = "https://api.telegram.org/bot"

def pappagallo(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        message = msg["from"]["first_name"]
        text = msg['text']

        bot.sendMessage(chat_id, text)


bot = telepot.Bot(TOKEN)
bot.message_loop(pappagallo) ##Messaggio loop

print('Listening ...')

#Ciclo infinito per tenerlo sempre vivo
while True:
        time.sleep(10)
