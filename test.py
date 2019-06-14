import telebot

bot = telebot.TeleBot("726408045:AAFq182AHNaNGIHOlmdTGhJZsYx3pMm1N-M")
@bot.message_handler(content_types=['text'])

def send_echo(message):
	bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, "Как челюсть, Санечка")
bot.polling( none_stop = True)

input()

