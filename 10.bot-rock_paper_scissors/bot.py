import telebot
import random
from telebot import types

bot = telebot.TeleBot(token) # В переменную 'token' поместить токен бота

@bot.message_handler(commands=["start"])
def start(message, res=False):
    # Добавляем кнопки
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    # TODO добавить 3 объекта KeyboardButton для 'Камень','Ножницы','Бумага'
    item1=types.KeyboardButton("Камень")
    item2=types.KeyboardButton("Ножницы")
    item3=types.KeyboardButton("Бумага")
    # TODO добавить кнопки в клавиатуру (markup)
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'Нажми кнопку и начни игру ', reply_markup=markup)

points_me = 0 #Счётчик очков для игрока
points_bot = 0 #Счётчик очков для бота

@bot.message_handler(content_types=["text"])
def handle_text(message):
    # TODO посылать в чат случайное из списка 'Камень','Ножницы','Бумага'
    answers = ['Камень','Ножницы','Бумага']
    answer = random.choice(answers)
    global points_me
    global points_bot
    if message.text == "Камень":
        if answer == "Камень":
            result = 'Ничья'
            points_bot += 1
            points_me += 1
        elif answer == 'Ножницы':
            result = 'Вы выиграли'
            points_me += 1
        else:
            result = 'Вы проиграли'
            points_bot += 1
    if message.text == "Ножницы":
        if answer == "Ножницы":
            result = 'Ничья'
            points_bot += 1
            points_me += 1
        elif answer == 'Бумага':
            result = 'Вы выиграли'
            points_me += 1
        else:
            result = 'Вы проиграли'
            points_bot += 1
    if message.text == "Бумага":
        if answer == "Бумага":
            result = 'Ничья'
            points_bot += 1
            points_me += 1
        elif answer == 'Камень':
            result = 'Вы выиграли'
            points_me += 1
        else:
            result = 'Вы проиграли'
            points_bot += 1
    bot.send_message(message.chat.id, f'{answer}\n{result}\nОбщий счёт:\nБот- {points_bot}\nВы- {points_me}')

bot.polling(none_stop=True, interval=0)  
