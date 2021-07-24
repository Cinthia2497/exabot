import os
import telebot

TOKEN = '1889540463:AAEMZQOQAqWPRnAUfXuvt3goIhBoxi3sIjU'

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['form'])

def foto(m):
    cid=m.chat.id
    bot.send_photo(cid, open('formula.jpg','rb'))

@bot.message_handler(commands=['formulas'])

def imagen(m):
    cid=m.chat.id
    bot.send_photo(cid, open('formlas.png','rb'))


@bot.message_handler(commands=['pdf'])

def pdf(m):
    cid=m.chat.id
    bot.send_document(cid, open('t20.pdf','rb'))

@bot.message_handler(commands=['ubicacion','localizacion'])
def ubicacion(m):
    cid=m.chat.id
    bot.send_location(cid, 15.49560, -87.99128)
bot.polling()

bot.polling()

