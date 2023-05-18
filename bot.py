import telebot
from telebot import types# берем из бибилиотеки telebot метод types, который нужен для работы с меню бота

bot = telebot.TeleBot('6155271972:AAGf_ZVghIURhFRCYAmB8h6YpRgWMXr7eBk')#создаем перем. bot и сохраняем туда созданный класс telebota,
#внутри скобок указываем api, уникальный адресс

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)#создаем объект меню при помощи types метода ReplyKeyboardMarkup
btn1 = types.KeyboardButton('Список фильмов')#обращаемся к types создаем кнопки при помощи метода KeyboardButton
btn2 = types.KeyboardButton('Список сериалов')
btn3 = types.KeyboardButton('Список аниме')
main_menu.add(btn1, btn2, btn3)#после того, как мы создали 3 кнопки, мы закидываем эти кнопки в переменную main_menu выше

# Обработчик команды /start
@bot.message_handler(commands=['start'])#дикаратор, который помогает обработывать команды в боте. Припиывает функции к дикартору ниже
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я бот для работы с фильмами, сериалами и аниме. Выбери пункт меню:", reply_markup=main_menu)
#send_message отправляет сообщения в чат бота
@bot.message_handler(content_types=['text'])# тот же самый дикартор, но для обработки текста
def get_text_messages(message):#создаем фуннции для обработки текста из чата, для того чтобы реагировать на сообщения из меню
    if message.text == "Список фильмов":#обращаемся к переменный message и обращаемся к методу text, чтобы оббработать сообщения из часта
        sp_films = ["kinopoisk.ru", "ivi.ru", "more.tv"]#если сообщение ровно список фильмов, то мы создаем список и туда вписываем ссылки на фильмы
        mess = ""#создал переменную, которая будет собирать, по прядку с переносм строки элементы из списка
        for element in sp_films:#через цикл мы обращаемся к списку к каждому элементу
        	mess = mess + element + "\n"#в переменную mess запиши элемент из списка и добавь перенос строки /n
        bot.send_message(message.from_user.id, mess)#после цикла, отправляем нашу переменную mess в чат бот при помощи метода send_message
    elif message.text == "Список сериалов":#если у нас не было списков фильмов, то он смотрет уже список сериалов
        sp_serial = ["kinopoisk.ru", "ivi.ru", "more.tv","doramy.club"]
        mess = ""
        for element in sp_serial:
            mess = mess + element + "\n"
        bot.send_message(message.from_user.id, mess)
    elif message.text == "Список аниме":
        sp_anime = ["v2.vost.pw", "animego.org", "yummyani.me"]
        mess = ""
        for element in sp_anime:
            mess = mess + element + "\n"
        bot.send_message(message.from_user.id, mess)

bot.polling(none_stop=True, interval=0)#Чтобы бот работал