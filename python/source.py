import telebot
import config # Файл с токеном бота
import random
from findanek import find_anekdot
from telebot import types

bot = telebot.TeleBot(config.token)

# Функция для создания кнопок
def create_markup(names):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard = True)
    for i in names:
        markup1.add(types.KeyboardButton(i))
    return markup1

# Обработка команды /start
@bot.message_handler(commands=['start'])
def starter(message):
    markup = create_markup(['расскажи анекдот'])
    bot.send_message(message.chat.id,
                     f'<i>Привет, <b>{message.from_user.first_name}</b>, я могу рассказать тебе анекдот!</i>', parse_mode='html', reply_markup = markup)

# Обработка текстовых команд
@bot.message_handler(content_types=['text'])
def get_commands(message):
    if(message.text == 'расскажи анекдот'):
        anek = find_anekdot()
        bot.send_message(message.chat.id, anek)
        print(anek)
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю')

# Запуск бота
while True:
    try:
        if __name__ == '__main__':
            bot.infinity_polling()

        #ConnectionError and ReadTimeout because of possible timout of the requests library
        #TypeError for moviepy errors
        #maybe there are others, therefore Exception

    except Exception as e:
        logger.error(e)
        time.sleep(15)
