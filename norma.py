import telebot
from telebot import types


api = '1985311086:AAFYYhOpVf5UDdwwLb6UZ3XC_PV0_twZLA8'

marking = 'Маркировка - нанесение на упаковку или этикетку сгенерированного цифрового кода: электронного точечного двухмерного кода формата Data Matrix. Основной целью маркировки товаров является повышение защиты и снижение оборота фальсифицированной и контрафактной продукции.'
kkm = 'ККМ (Контрольно-кассовая машина) - аппаратно-программные средства с фискальной памятью или программное обеспечение с функцией фиксации, некорректируемой ежесуточной (ежесменной) регистрацией, долговременного хранения и передачи данных в режиме реального времени в уполномоченный налоговый орган в защищенном виде.'
ofd = 'ОФД (Оператор фискальных данных) – это организация, обеспечивающая технический процесс сбора и передачи данных в защищенном виде только уполномоченному налоговому органу или оператору национальной системы маркировки и прослеживаемости маркированных товаров в Кыргызской Республике.'


bot = telebot.TeleBot(api)

keyboard_1 = telebot.types.ReplyKeyboardMarkup(True)

btn_1 = telebot.types.KeyboardButton('Маркировка')
btn_2 = telebot.types.KeyboardButton('ККМ')
btn_3 = telebot.types.KeyboardButton('ОФД')
btn_4 = telebot.types.KeyboardButton('Автоматизация магазина')
btn_5 = telebot.types.KeyboardButton('Больше информации!')

keyboard_1.row(btn_1, btn_2)
keyboard_1.row(btn_3, btn_4)
keyboard_1.row(btn_5)



@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='http://www.norma.kg/')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вас приветствует Группа Компаний «Новая Норма»! ', reply_markup=keyboard_1)


@bot.message_handler(content_types=['text'])
# def info_message(message):
#     bot.send_message(message.chat.id, , reply_markup=keyboard_1)
def send_text(message):
    if message.text.lower() == 'маркировка':
        bot.send_photo(chat_id=message.chat.id, caption=marking, photo='http://www.norma.kg/static/media/Rectangle%2063.40da64e4.png', reply_markup=keyboard_1)
    if message.text.lower() == 'ккм':
        bot.send_photo(chat_id=message.chat.id, caption=kkm, photo='https://smebanking.news/ru/wp-content/uploads/sites/2/2018/10/online-kassa.jpg', reply_markup=keyboard_1)
        # bot.send_photo(chat_id=message.chat.id, photo='http://www.norma.kg/static/media/pic1.b9546ea8.png')
    if message.text.lower() == 'офд':
            bot.send_photo(chat_id=message.chat.id, caption=ofd, photo='http://www.norma.kg/static/media/Rectangle%2016.bea67cda.png', reply_markup=keyboard_1)
            # bot.send_photo(chat_id=message.chat.id, photo='http://www.norma.kg/static/media/Rectangle%2016.bea67cda.png')
    if message.text.lower() == 'автоматизация магазина':
                bot.send_photo(chat_id=message.chat.id, caption='Установка товаро-учетных систем:\n- 1С;\n- Мой Склад и т.д.',
                      photo='https://brigit.com.ua/wp-content/uploads/retail.jpg', reply_markup=keyboard_1)
    #             bot.send_photo(chat_id=message.chat.id, photo='http://www.norma.kg/static/media/pic1.b9546ea8.png')
    if message.text == 'Больше информации!':
            bot.send_message(chat_id=message.chat.id, text='Номер нашего call-центра: +996501588882\n'
                    'Наш сайт: http://www.norma.kg/\n'
                    'Эл. почта: nnormakg@gmail.com\n'
                    'inst : https://www.instagram.com/norma.kg/?hl=ru ', reply_markup=keyboard_1)

@bot.message_handler(content_types=['text'])
def go_txt(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Здраствуйте!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Всего доброго!')
    elif message.text == 'ха-ха':
        bot.send_sticker(message.chat.id, 'CAADAgADcwgAAhhC7ggBnQGJ6b93ggI')
    else:
        bot.send_message(message.chat.id, 'Я Вас не понимаю ')

bot.polling()
