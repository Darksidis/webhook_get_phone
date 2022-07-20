token = '5525500034:AAG5i4XrlPtq_GeeIx4eldOjxcGgu0syz24'
import telebot
from telebot import types
from credietienals import *
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text='Отправить телефон', request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Номер телефона',reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        print (message.chat.username)
        print(message.contact)



bot.polling()


