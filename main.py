import telebot
from telebot import types
import random

TOKEN = "///"
bot = telebot.TeleBot(TOKEN)

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Факт о космосе")
    keyboard.add("Планеты", "Help")
    return keyboard

def planets_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Меркурий", "Венера")
    keyboard.add("Земля", "Марс")
    keyboard.add("Юпитер", "Сатурн")
    keyboard.add("Уран", "Нептун")
    keyboard.add("Назад")
    return keyboard

facts = ["Вселенная расширяется.","Свет от Солнца до Земли летит примерно 8 минут.","В космосе нет звука, потому что там нет воздуха.","В нашей галактике Млечный Путь — сотни миллиардов звёзд.","Чёрные дыры искривляют пространство и время.","Самая высокая гора в Солнечной системе — Олимп на Марсе.","Венера горячее Меркурия, хотя дальше от Солнца.","Юпитер настолько большой, что в него поместились бы все планеты.","Луна всегда повернута к Земле одной стороной.","Вселенной примерно 13,8 миллиарда лет."]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, космонавт!\n""Меня зовут Голос Веленной.\n""О чем хочешь поговорить?\n""Выбери действие:",reply_markup=main_keyboard())

@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text
    if text == "Привет" or text == "Здрасте" :
        bot.send_message(message.chat.id, "Привет, космонавт!\nМогу рассказать интересный факт о Вселенной!\nВыбери действие:",reply_markup=main_keyboard())
    elif text == "Факт о космосе":
        bot.send_message(message.chat.id, random.choice(facts))
    elif text == "Планеты":
        bot.send_message(message.chat.id,"Выбери планету:",reply_markup=planets_keyboard())
    elif text == "Меркурий":
        bot.send_message(message.chat.id,"Меркурий - самая близкая к Солнцу и самая маленькая планета Солнечной системы. У него почти нет атмосферы, поэтому температура сильно меняется: от сильного холода ночью до экстремальной жары днём. Год на Меркурии длится около 88 земных дней.")
    elif text == "Венера":
        bot.send_message(message.chat.id,"Венера - вторая планета от Солнца и самая горячая в Солнечной системе. Её плотная атмосфера состоит в основном из углекислого газа и создаёт мощный парниковый эффект. Венера вращается вокруг своей оси в обратном направлении по сравнению с большинством планет.")
    elif text == "Земля":
        bot.send_message(message.chat.id,"Земля - третья планета от Солнца и единственная известная планета, на которой существует жизнь. На Земле есть жидкая вода, подходящая атмосфера и магнитное поле. У Земли один естественный спутник — Луна.")
    elif text == "Марс":
        bot.send_message(message.chat.id,"Марс - четвёртая планета от Солнца, известная своим красным цветом из-за оксида железа в почве. На Марсе есть полярные ледяные шапки и следы воды в прошлом. Он считается одной из самых перспективных планет для будущих исследований и возможного освоения.")
    elif text == "Юпитер":
        bot.send_message(message.chat.id,"Юпитер - крупнейшая планета Солнечной системы и газовый гигант. Он известен Большим Красным Пятном — гигантским штормом, который длится сотни лет. У Юпитера десятки спутников, включая самый большой — Ганимед.")
    elif text == "Сатурн":
        bot.send_message(message.chat.id,"Сатурн - газовый гигант, легко узнаваемый благодаря своей системе колец. Он имеет очень низкую среднюю плотность и множество спутников. Самый известный из них — Титан, обладающий плотной атмосферой.")
    elif text == "Уран":
        bot.send_message(message.chat.id,"Уран - ледяной гигант, который вращается вокруг Солнца, «лежа на боку». Его голубой цвет связан с наличием метана в атмосфере. Уран является одной из самых холодных планет Солнечной системы.")
    elif text == "Нептун":
        bot.send_message(message.chat.id,"Нептун - самая дальняя планета от Солнца и ледяной гигант. Он известен самыми сильными ветрами в Солнечной системе. Один год на Нептуне длится около 165 земных лет.")
    elif text == "Назад":
        bot.send_message(message.chat.id,"Ты вернулся в главное меню",reply_markup=main_keyboard())
    elif text == "Help":
        bot.send_message(message.chat.id,"Используй кнопки внизу, чтобы общаться с ботом.")
    else:
        bot.send_message(message.chat.id,"Используй кнопки",reply_markup=main_keyboard())
bot.infinity_polling(timeout=10, long_polling_timeout=5)
