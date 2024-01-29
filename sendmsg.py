import telebot
from dotenv import load_dotenv
import os


load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
chat_id = os.getenv('CHAT_ID')
contact_list = [('zip_code', 'Индекс'), ('address', 'Адрес'),
                ('phone', 'Телефон'), ('customer_name', 'Имя'), ('order_id', '# заказа')]


def sendmsg(mylist):
    sep_line = '-' + 15 * 'x-'
    delivery, sum_total, txt = 0, 0, ''

    for i in range(-1, -6, -1):
        txt1 = f"{contact_list[i][1]}: <b>{mylist[i][contact_list[i][0]]}</b>"
        bot.send_message(chat_id, text=txt1, parse_mode='HTML')

    if mylist[-6]['delivery'] == 'y':
        delivery = 5

    for wine in mylist[:-6]:
        txt += f"<b>{wine['wine_id']}</b> <b>{wine['title']}</b>: {wine['price']}€ x <b>{wine['amount']}</b>\n"
        sum_total += wine['price'] * wine['amount']

    sum_total += delivery
    txt += f"Доставка: {delivery}€\nОбщая сумма <b>{round(sum_total, 1)}€</b>"
    bot.send_message(chat_id, text=txt, parse_mode='HTML')
    bot.send_message(chat_id, text=sep_line)


def send_error_message(error_message):
    max_length = 1024
    sep_line = '❗' + 15 * '🆘❗' + '🆘'

    bot.send_message(chat_id, text=sep_line)
    while error_message:
        text_msg = error_message[:max_length]
        bot.send_message(chat_id, text=text_msg)
        error_message = error_message[max_length:]
    bot.send_message(chat_id, text=sep_line)
