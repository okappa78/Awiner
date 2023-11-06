import telebot
from dotenv import load_dotenv
import os


load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
chat_id = os.getenv('CHAT_ID')
contact_list = [('zip_code', 'Индекс'), ('address', 'Адрес'),
                ('phone', 'Телефон'), ('name', 'Имя'), ('order_id', '# заказа')]


def sendmsg(mylist):
    delivery, sum_total, txt = 0, 0, ''

    for i in range(-1,-6,-1):
        txt1 = f"{contact_list[i][1]}: <b>{mylist[i][contact_list[i][0]]}</b>"
        bot.send_message(chat_id, text=txt1, parse_mode='HTML')

    if mylist[-6]['delivery'] == 'y':
        delivery = 5

    for wine in mylist[:-6]:
        txt += f"<b>{wine['title']}</b>: {wine['price']}€ x <b>{wine['amount']}</b>\n"
        sum_total += wine['price'] * wine['amount']

    txt += f"Доставка: {delivery}€\nОбщая сумма <b>{sum_total + delivery}€</b>"
    bot.send_message(chat_id, text=txt, parse_mode='HTML')