import telebot
from telebot import types
import my_dict
import json
from dotenv import load_dotenv
import os
from selection import get_filtered
from getwine import getwine, getphoto
from addtodb import add_to_db_filters, add_to_db_carts
from cart import get_numbers, get_address, get_phone, get_orderid
from sendmsg import sendmsg
import threading

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
users_wine = {}
users_cart = {}
prev_messages = {}


def print_test():
    print('users', users)
    print('users_cart', users_cart)
    print('users_wine', users_wine)


def show_return_lang_button(*before_btns):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if None not in before_btns:
        for btn in before_btns:
            markup.add(btn)
    btn_return = types.KeyboardButton(text=my_dict.return_button)
    markup.add(btn_return)
    return markup


def show_language_selection(user_id):
    users[user_id]['step'] = 1

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(user_id,
                     text=my_dict.choose_lang,
                     reply_markup=markup)


def intro_message(user_id):
    lang = users[user_id]['lang']

    markup = show_return_lang_button()

    bot.send_message(user_id, text=my_dict.intro_message[lang])
    bot.send_message(user_id, text=my_dict.help_message[lang])
    bot.send_message(user_id, text=my_dict.ai_message[lang], reply_markup=markup)


def reset_filters(user_id):
    step = users[user_id]['step']
    length = len(my_dict.dict_steps) + 1

    # Если пользователь подтвердил все фильтры, то после их обработки, удаляем все фильтры
    if step == 7:
        step = 1
    # Проверка на возврат к выбору Розового вина и вероятные ошибки
    elif users[user_id].get('wine_type', None) == 'rose' and step < 5:
        step = 2

    for i in range(step, length):
        users[user_id].pop(my_dict.dict_steps[i][0], None)


def show_menu_step(user_id):
    reset_filters(user_id)  # удаляем все значения фильтра (если они есть),
                            # которые последовательно идут после этого stepa

    lang = users[user_id]['lang']
    step = users[user_id]['step']
    options = my_dict.dict_categories[my_dict.dict_steps[step][0]]

    if step == 2 or step == 4:
        wtype = users[user_id].get('wine_type', None)
        if wtype is None:
            users[user_id]['step'] = 1
            bot.send_message(user_id, text=my_dict.error_msg[lang])
            return show_menu_step(user_id)

        options = options[wtype]

    elif step == 5:
        wstyle = users[user_id]['wine_style']
        wsugar = users[user_id]['wine_sugar']
        wcountry = users[user_id]['wine_country']
        options = options[wstyle][wsugar][wcountry]

    markup = types.InlineKeyboardMarkup(row_width=1)
    for i, option in enumerate(options[lang]):
        button = types.InlineKeyboardButton(option,
                                            callback_data=options[-1][i])
        markup.add(button)

    if step == 5:
        button = types.InlineKeyboardButton(text=my_dict.skip_text[lang],
                                            callback_data='skip')
        markup.add(button)

    bot.send_message(user_id,
                     text=my_dict.dict_messages[step][lang],
                     reply_markup=markup)


def restart_choose_wine(user_id):
    try:
        lang = users[user_id]['lang']
        btn_cart = None
        if users[user_id].get('wine_cart', None):
            btn_cart = types.KeyboardButton(text=my_dict.btn_cart[lang])
        markup = show_return_lang_button(btn_cart)
        bot.send_message(user_id,
                         text=my_dict.restart_text[lang],
                         reply_markup=markup)

        users[user_id]['step'] = 1
        show_menu_step(user_id)
    except KeyError:
        bot.send_message(user_id, text=my_dict.error_msg[lang])
        show_language_selection(user_id)

def confirm_message(user_id):
    lang = users[user_id]['lang']
    text_message = [['Ваш выбор: ', 'You choose: '][lang]]
    for i in range(1, 7):
        step_val = my_dict.dict_steps[i]
        if step_val[0] in users[user_id]:
            fltr_point = f'{step_val[1][lang]}' \
                         + f'<b>{my_dict.terms[step_val[0]][users[user_id][step_val[0]]][lang]}</b>'
            text_message.append(fltr_point)

    bot.send_message(user_id,
                     text=my_dict.wine_suggest_message[lang])
    bot.send_message(user_id,
                     text='\n\n'.join(text_message), parse_mode='HTML')


def check_mandatory_cats(user_id):
    try:
        users[user_id]['wine_type']
        if users[user_id]['wine_type'] == 'rose'\
            and all(key in users[user_id] for key in my_dict.mandatory_cats_rose):
            return True
        elif all(key in users[user_id] for key in my_dict.mandatory_cats):
            return True
        else:
            return False
    except KeyError:
        return False


def confirm_filter(user_id):
    lang = users[user_id]['lang']

    btn1 = types.KeyboardButton(text=my_dict.confirm_button[lang])
    btn2 = types.KeyboardButton(text=my_dict.restart_button[lang])
    markup = show_return_lang_button(btn1, btn2)

    bot.send_message(user_id,
                     text=my_dict.confirm_fltr_msg[lang],
                     reply_markup=markup)


def filter_wines(user_id):
    lang = users[user_id]['lang']

    btn_restart = types.KeyboardButton(text=my_dict.restart_button[lang])
    markup = show_return_lang_button(btn_restart)
    bot.send_message(user_id,
                     text=my_dict.show_wines_msg[lang],
                     reply_markup=markup)

    wineid_out = get_filtered(users[user_id])
    reset_filters(user_id)
    if not wineid_out:
        bot.send_message(user_id,
                         text=my_dict.empty_res_msg[lang])
    else:
        list_of_wines = getwine(wineid_out, user_id, lang=lang)
        list_of_wines[user_id].append(0) #устанавливаем индекс для показа отфильтрованных вин
        users_wine.update(list_of_wines)
        send_description(user_id)


def send_description(user_id):
    index = users_wine[user_id][-1]
    lang = users[user_id]['lang']
    wine = users_wine[user_id][index]

    if user_id in prev_messages:
        bot.delete_message(user_id, prev_messages[user_id])

    description_text = f"({index + 1}/{len(users_wine[user_id]) - 1}) {wine['wine_id']}\n{wine['description']}"[:400]

    markup = types.InlineKeyboardMarkup(row_width=2)
    prev_button = types.InlineKeyboardButton(my_dict.bwd_button[lang], callback_data='prev')
    cart_button = types.InlineKeyboardButton(my_dict.cart_button[lang], callback_data='cart')
    next_button = types.InlineKeyboardButton(my_dict.fwd_button[lang], callback_data='next')
    markup.add(prev_button, next_button, cart_button)

    photo_url = getphoto(wine['wine_id'])
    sent_message = bot.send_photo(user_id, photo_url, caption=description_text, reply_markup=markup)
    prev_messages[user_id] = sent_message.message_id


def add_to_cart(user_id):
    lang = users[user_id]['lang']
    index = users_wine[user_id][-1]
    wine = users_wine[user_id][index]
    users[user_id].setdefault('wine_cart', set()).add(wine['wine_id'])  # wine_id тип str !!!!
    users[user_id]['step'] = 8

    btn_restart = types.KeyboardButton(text=my_dict.restart_button[lang])
    btn_cart = types.KeyboardButton(text=my_dict.btn_cart[lang])
    markup = show_return_lang_button(btn_restart, btn_cart)

    txt_add_cart = f"{my_dict.confirm_carts_msg[lang]}\n{wine['title']}"
    message_to_delete = bot.send_message(user_id, text=txt_add_cart, reply_markup=markup)


def send_cart_message(user_id):
    step = users[user_id]['step']
    lang = users[user_id]['lang']
    wines = users_cart[user_id]
    text_message = [['Ваша корзина: ', 'Your cart: '][lang]]

    for i, w in enumerate(wines, 1):
        point = f"<b>{i}. {w['title']}, {w['price']}.00 €</b>"
        if 'amount' in w:
            point += f"<b> - {w['amount']}{['шт', 'qty'][lang]}</b>"
            if w['amount'] == 0:
                point = f"<s>{point}</s>"

        text_message.append(point)

    if step == 9:
        bot.send_message(user_id,
                         text=my_dict.wine_cart_msg[lang])
        bot.send_message(user_id,
                         text=my_dict.delivery_price_msg[lang])

    # Показываем кнопки Начать заново и Выбор языка
    btn = types.KeyboardButton(text=my_dict.restart_button[lang])
    markup = show_return_lang_button(btn)

    bot.send_message(user_id,
                     text='\n\n'.join(text_message), parse_mode='HTML', reply_markup=markup)

    if step == 10:
        cart_amount = sum([w['price'] * w['amount'] for w in wines])
        del_flag = int(cart_amount < 30)
        delivery = ['0€', '5€'][del_flag]
        total = cart_amount + (0, 5)[del_flag]
        users_cart[user_id].append({'delivery': ('n', 'y')[del_flag]})

        txt = f"{my_dict.cart_summary_msg[lang]} <b>{cart_amount}€</b>\n"+\
              f"{['Доставка:', 'Delivery:'][lang]} <b>{delivery}</b>\n"+\
              f"{['Итого:', 'Total:'][lang]} <b>{total}€</b>"

        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        order_button = types.InlineKeyboardButton(my_dict.order_button[lang], callback_data='order')
        markup_inline.add(order_button)
        bot.send_message(user_id, text=txt, parse_mode='HTML', reply_markup=markup_inline)
        bot.send_message(user_id, text=my_dict.edit_qty_msg)


def get_amount(user_id, numbers):
    lang = users[user_id]['lang']
    step = users[user_id]['step']
    users_cart[user_id] = users_cart[user_id] if step == 9 else users_cart[user_id][:-1]
    wine_quantity = len(users_cart[user_id])
    num_list = get_numbers(numbers, wine_quantity)

    if not num_list:
        bot.send_message(user_id,
                         text=my_dict.error_quant_msg[lang])

    else:
        print(users_cart[user_id])
        print(num_list)
        for i, w in enumerate(users_cart[user_id]):
            w['amount'] = num_list[i]
        users[user_id]['step'] = 10
        send_cart_message(user_id)


def confirm_ordering(user_id):
    lang = users[user_id]['lang']
    order_id = get_orderid()
    users_cart[user_id].append({'order_id': order_id})
    txt = f"{['# заказа: ', '# order: '][lang]}<b>{order_id}</b>\n" + my_dict.ordering_confirm_msg[lang]
    bot.send_message(user_id, text=txt, parse_mode='HTML')
    return show_language_selection(user_id)


def add_data_to_order(user_id, data):
    step = users[user_id]['step']
    lang = users[user_id]['lang']
    try:
        users_cart[user_id]
        if step == 11:
            users_cart[user_id][:-1] = [wine for wine in users_cart[user_id][:-1] if wine['amount'] > 0]
            zip_code = get_address(data)
            users_cart[user_id].append({'zip_code': zip_code})
            users_cart[user_id].append({'address': data})
        elif step == 12:
            data = get_phone(data)
            if not data:
                return bot.send_message(user_id, text=['Неверый ввод', 'Wrong data'][lang])
            users_cart[user_id].append({'phone': data})
        elif step == 13:
            users_cart[user_id].append({'name': data})

        users[user_id]['step'] += 1

    except KeyError:
        bot.send_message(user_id, text=my_dict.error_msg[lang])
        restart_choose_wine(user_id)


def ordering_address(user_id):
    step = users[user_id]['step']
    lang = users[user_id]['lang']
    if step == 11:
        bot.send_message(user_id, text=my_dict.ordering_address_msg[lang])
    elif step == 12:
        bot.send_message(user_id, text=my_dict.ordering_phone_msg[lang])
    elif step == 13:
        bot.send_message(user_id, text=my_dict.ordering_name[lang])


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    users[user_id] = {}

    show_language_selection(user_id)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print_test()
    user_id = message.from_user.id
    step = users.setdefault(user_id, {'step': 0})['step']

    if step < 1:
        show_language_selection(user_id)

    else:

        if message.text == '🇷🇺 Русский':
            users[user_id]['lang'] = 0
            #with open('userspref.json', 'w') as file:
            #    json.dump(users, file)

            intro_message(user_id)
            show_menu_step(user_id)

        elif message.text == '🇬🇧 English':
            users[user_id]['lang'] = 1
            #with open('userspref.json', 'w') as file:
            #    json.dump(users, file)

            intro_message(user_id)
            show_menu_step(user_id)

        elif message.text in my_dict.return_button:
            show_language_selection(user_id)

        elif message.text in my_dict.restart_button:
            users_wine.pop(user_id, None)
            restart_choose_wine(user_id)

        elif message.text in my_dict.confirm_button:
            try:
                users[user_id]['wine_price']

                #t = threading.Thread(target=add_to_csv_filters, args=(user_id, users[user_id]))
                t = threading.Thread(target=add_to_db_filters, args=(user_id, users[user_id]))
                t.start()

                users[user_id]['step'] = 7
                filter_wines(user_id)

            except KeyError:
                users[user_id]['step'] = 1
                lang = users[user_id]['lang']
                bot.send_message(user_id, text=my_dict.error_msg[lang])
                show_menu_step(user_id)

        # ИДЕМ В КОРЗИНУ И РЕДАКТИРУЕМ КОЛИЧЕСТВО
        elif message.text in my_dict.btn_cart:
            users[user_id]['step'] = 9
            users_wine.pop(user_id, None)
            cart_wineids = list(map(int, users[user_id]['wine_cart']))
            list_for_cart = getwine(cart_wineids, user_id, complete=False)
            users_cart.update(list_for_cart)
            send_cart_message(user_id)

        else:
            if step == 9 or step == 10:
                get_amount(user_id, message.text)
            elif step == 11:
                contact_data = message.text
                add_data_to_order(user_id, contact_data)
                #users[user_id]['step'] = 12
                ordering_address(user_id)
            elif step == 12:
                contact_data = message.text
                add_data_to_order(user_id, contact_data)
                ordering_address(user_id)
            elif step == 13:
                contact_data = message.text
                add_data_to_order(user_id, contact_data)
                confirm_ordering(user_id)
                sendmsg(users_cart[user_id])

                #t = threading.Thread(target=add_to_csv_cart, args=(user_id, users_cart[user_id]))
                t = threading.Thread(target=add_to_db_carts, args=(user_id, users_cart[user_id]))
                t.start()

                del users[user_id]['wine_cart']
                del users_cart[user_id]
                print('Ordering!!!')
                print_test()



@bot.callback_query_handler(func=lambda call: True)
def get_call(call):
    print_test()
    user_id = call.message.chat.id
    step = users.setdefault(user_id, {'step': 0})['step']

    if step < 1:
        show_language_selection(user_id)

    else:

        lang = users[user_id]['lang']

        #check wine type
        if call.data in my_dict.terms['wine_type']:
            #users[user_id].pop('wine_grape', None)
            users[user_id]['wine_type'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wine_type'][users[user_id]['wine_type']][lang]}")

            if call.data == 'rose':
                users[user_id]['wine_type'] = call.data
                users[user_id]['step'] = 4


            else:
                users[user_id]['step'] = 2

            show_menu_step(user_id)

        #check wine style
        elif call.data in my_dict.terms['wine_style']:
            #users[user_id].pop('wine_grape', None)
            users[user_id]['wine_style'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wine_style'][users[user_id]['wine_style']][lang]}")

            # КОСТЫЛЬ!!! Разобраться!!!
            users[user_id]['wine_type'] = users[user_id]['wine_style'].split('_')[-1]

            users[user_id]['step'] = 3
            show_menu_step(user_id)

        #check sugar in wine
        elif call.data in my_dict.terms['wine_sugar']:
            #users[user_id].pop('wine_grape', None)
            users[user_id]['wine_sugar'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wine_sugar'][users[user_id]['wine_sugar']][lang]}")

            users[user_id]['step'] = 4
            show_menu_step(user_id)

        #check country
        elif call.data in my_dict.terms['wine_country']:
            users[user_id]['wine_country'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wine_country'][users[user_id]['wine_country']][lang]}")

            if users[user_id].get('wine_sugar', None) == 'dry'\
                    or (users[user_id].get('wine_sugar', None) == 'semi_dry'
                        and users[user_id].get('wine_type', None) == 'white'):
                    users[user_id]['step'] = 5
            else:
                users[user_id]['step'] = 6

            show_menu_step(user_id)

        # check grapes
        elif call.data in my_dict.terms['wine_grape']:
            users[user_id]['wine_grape'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wine_grape'][users[user_id]['wine_grape']][lang]}")

            users[user_id]['step'] = 6
            show_menu_step(user_id)

        #check skip option
        elif call.data == 'skip' and step == 5:
            users[user_id]['step'] = 6
            show_menu_step(user_id)

        # check price
        elif call.data in my_dict.terms['wine_price']:
            users[user_id]['wine_price'] = call.data

            if check_mandatory_cats(user_id):
                confirm_message(user_id)
                confirm_filter(user_id)
            else:
                users[user_id]['step'] = 1
                lang = users[user_id]['lang']
                markup = show_return_lang_button()
                if user_id in users_cart:
                    btn_cart = types.KeyboardButton(text=my_dict.btn_cart[lang])
                    markup = show_return_lang_button(btn_cart)
                bot.send_message(user_id, text=my_dict.more_cats_msg[lang], reply_markup=markup)
                show_menu_step(user_id)

        elif call.data == 'prev' and users_wine:
            users_wine[user_id][-1] = max(0, users_wine[user_id][-1] - 1)
            send_description(user_id)
        elif call.data == 'next' and users_wine:
            users_wine[user_id][-1] = min(len(users_wine[user_id]) - 2, users_wine[user_id][-1] + 1)
            send_description(user_id)

        elif call.data == 'cart' and users_wine:
            add_to_cart(user_id)

        elif call.data == 'order':
            users[user_id]['step'] = 11
            bot.send_message(user_id, text=my_dict.ordering_msg[lang])
            ordering_address(user_id)




if __name__ == '__main__':
    users = {}

    bot.polling(none_stop=True, interval=0)