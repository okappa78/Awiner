import telebot
from telebot import types
from dotenv import load_dotenv
import os
import threading

import my_dict
from getfromdb import get_description, get_photo
from getfromdb_alt import get_filtered, check_exist_address
from addtodb import add_to_db_filters, add_to_db_carts, add_to_db_customers
from cart import get_numbers, get_address, get_phone, get_orderid
from sendmsg import sendmsg

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
users_wine = {}
users_cart = {}
prev_messages = {}


def print_test():
    print('users', users)
    print('users_cart', users_cart)
    print('users_wine', users_wine)
    print('prev_messages:', prev_messages)


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

    btn_cart = None
    if users[user_id].get('wine_cart', None):
        btn_cart = types.KeyboardButton(text=my_dict.btn_cart[lang])
    markup = show_return_lang_button(btn_cart)

    bot.send_message(user_id, text=my_dict.intro_message[lang])
    bot.send_message(user_id, text=my_dict.help_message[lang], reply_markup=markup)
    # bot.send_message(user_id, text=my_dict.ai_message[lang], reply_markup=markup)


def reset_filters(user_id):
    step = users[user_id]['step'] if users[user_id]['step'] < 50 else 5
    length = 7

    # Если пользователь подтвердил все фильтры, то после их обработки, удаляем все фильтры
    if step == 7:
        step = 1
    # Проверка на возврат к выбору Розового вина и вероятные ошибки
    elif users[user_id].get('wtype', None) in ('rose', 'fortified') and step < 5:
        step = 2

    for i in range(step, length):
        users[user_id].pop(my_dict.dict_steps[i][0], None)
        if i == 5:
            users[user_id].pop('grape', None)
            users[user_id].pop('region', None)


def show_menu_step(user_id):
    lang = users[user_id]['lang']
    step = users[user_id]['step']
    options = my_dict.dict_categories[my_dict.dict_steps[step][0]]

    # удаляем все значения фильтра (если они есть),
    # которые последовательно идут после этого stepa
    reset_filters(user_id)

    # список, в который будут помещаться кнопки
    btns = []

    if step > 1:
        try:
            wtype = users[user_id]['wtype']
            if step == 2 and wtype == 'orange':
                options = [option[1:] for option in options]
            elif step == 3:
                if wtype == 'sparkling':
                    options = [option[:2] for option in options]
                else:
                    options = [option[1:] for option in options]
            elif step == 4:
                options = options[wtype]
            elif step == 51:
                wstyle = users[user_id]['wstyle']
                wcountry = users[user_id]['country']
                options = options[wtype][wstyle][wcountry]
                if len(options[lang]) < 2:
                    users[user_id]['step'] = 6
                    return show_menu_step(user_id)
            elif step == 52:
                wcountry = users[user_id]['country']
                options = options[wtype][wcountry]
                if len(options[lang]) < 2:
                    users[user_id]['step'] = 6
                    return show_menu_step(user_id)

        except:
            users[user_id]['step'] = 1
            bot.send_message(user_id, text=my_dict.error_msg[lang])
            return show_menu_step(user_id)

    # if step == 5:
    #    wstyle = users[user_id]['wstyle']
    #    wsugar = users[user_id]['sugar']
    #    wcountry = users[user_id]['country']
    #    options = options[wstyle][wsugar][wcountry]

    # задаем количество кнопок в ряду
    rw = 1 if len(options[-1]) < 5 or step == 6 else 2

    markup = types.InlineKeyboardMarkup(row_width=rw)
    for i, option in enumerate(options[lang]):
        btn = types.InlineKeyboardButton(option, callback_data=options[-1][i])
        btns.append(btn)
    markup.add(*btns)

    if step in (5, 51, 52):
        button = types.InlineKeyboardButton(text=my_dict.skip_text[lang],
                                            callback_data='skip')
        markup.add(button)

    bot.send_message(user_id,
                     text=my_dict.dict_messages[step][lang],
                     reply_markup=markup, parse_mode='HTML')


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
        bot.send_message(user_id, text=my_dict.error_msg[1])
        show_language_selection(user_id)


def confirm_message(user_id):
    lang = users[user_id]['lang']
    text_message = [['Ваш выбор: ', 'You choose: '][lang]]
    for i in (1, 2, 3, 4, 51, 52, 6):
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
        wtype = users[user_id]['wtype']
        if wtype in ('rose', 'fortified') and all(key in users[user_id] for key in my_dict.mandatory_cats_rose):
            return True

        elif wtype == 'sparkling' and all(key in users[user_id] for key in my_dict.mandatory_cats_sparkling):
            return True

        elif wtype == 'orange' and all(key in users[user_id] for key in my_dict.mandatory_cats_orange):
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

    try:
        wineid_out, ff = get_filtered(users[user_id])
        reset_filters(user_id)
        list_of_wines = get_description(wineid_out, user_id, lang=lang)
        # устанавливаем индекс для показа отфильтрованных вин
        list_of_wines[user_id].append(0)
        users_wine.update(list_of_wines)

        if not ff:
            ask_suggestion(user_id)
        else:
            show_wines(user_id)

    except RecursionError:
        bot.send_message(user_id, text=my_dict.empty_res_msg[lang])
        bot.send_message(user_id, text=my_dict.empty_req_msg[lang])


def ask_suggestion(user_id):
    lang = users[user_id]['lang']

    bot.send_message(user_id, text=my_dict.empty_res_msg[lang])
    markup = types.InlineKeyboardMarkup()
    suggest_btn = types.InlineKeyboardButton(my_dict.ok_button[lang], callback_data='offerme')
    markup.add(suggest_btn)
    bot.send_message(user_id, text=my_dict.empty_res_msg_alt[lang], reply_markup=markup)
    bot.send_message(user_id, text=my_dict.empty_res_msg_alt_change[lang])


def wine_template(index, lngth, lang, wine):
    # Create list with headers and dictionary
    lst_header = ['wine', 'maker', 'wtype', 'grape', 'region', 'price', 'bouquet', 'palate', 'food']
    dict_head = {}

    # Start description text from number of current position / amount of all position
    description_text = [f"{index + 1} "
                        f"{['из', 'of'][lang]} {lngth} "
                        f"{['найденных', 'found'][lang]}"]

    # Fill the dictionary for text output
    dict_head['wine'] = f"{['Вино:', 'Wine:'][lang]} <b>{wine.get('title', None)} " \
                        f"{wine.get('collection', '')}</b>".replace('None', '').rstrip()
    dict_head['maker'] = f"{['Пр-ль:', 'Producer:'][lang]} <i>{wine.get('maker', None)}</i>"
    dict_head['wtype'] = f"{['Тип:', 'Type:'][lang]} {wine.get('wtype', None)} {wine.get('wstyle', None)} " \
                         f"{wine.get('sugar', None)}, {wine.get('alcohol', None)}".replace(' None', '')
    dict_head['grape'] = f"{['Виноград:', 'Grape:'][lang]} {wine.get('grape', None)}"
    dict_head['region'] = f"{['Регион:', 'Region:'][lang]} {wine.get('country', None)}, {wine.get('region', None)}"
    if wine.get('subregion', None):
        dict_head['region'] += f", {wine.get('subregion', None)}"
    dict_head['price'] = f"{['Цена:', 'Price:'][lang]} <b>{wine.get('price', None)}0 €</b>"
    dict_head['bouquet'] = f"{['Аромат:', 'Bouquet:'][lang]} {wine.get('bouquet', None)}"
    dict_head['palate'] = f"{['Вкус:', 'Palate:'][lang]} {wine.get('palate', None)}"
    dict_head['food'] = f"{['Гастрономия:', 'Gastronomy:'][lang]} {wine.get('food', None)}"

    for header in lst_header:
        description_text.append(dict_head[header])

    return description_text


def show_wines(user_id):
    index = users_wine[user_id][-1]
    lang = users[user_id]['lang']
    wine = users_wine[user_id][index]

    # Delete the previous message
    if user_id in prev_messages:
        bot.delete_message(user_id, prev_messages[user_id])

    lngth = len(users_wine[user_id]) - 1

    description_txt = wine_template(index, lngth, lang, wine)

    # Convert the list of attr to the text for output
    description_text = '\n'.join(description_txt)

    markup = types.InlineKeyboardMarkup(row_width=2)
    prev_button = types.InlineKeyboardButton(my_dict.bwd_button[lang], callback_data='prev')
    cart_button = types.InlineKeyboardButton(my_dict.cart_button[lang], callback_data='cart')
    next_button = types.InlineKeyboardButton(my_dict.fwd_button[lang], callback_data='next')
    markup.add(prev_button, next_button, cart_button)

    photo_url = get_photo(wine['wine_id'])
    sent_message = bot.send_photo(user_id, photo_url, caption=description_text, reply_markup=markup, parse_mode='HTML')
    prev_messages[user_id] = sent_message.message_id

    return description_text


def add_to_cart(user_id):
    lang = users[user_id]['lang']
    index = users_wine[user_id][-1]
    wine = users_wine[user_id][index]
    users[user_id].setdefault('wine_cart', set()).add(wine['wine_id'])  # wine_id тип str !!!!
    users[user_id]['step'] = 8

    btn_restart = types.KeyboardButton(text=my_dict.restart_button[lang])
    btn_cart = types.KeyboardButton(text=my_dict.btn_cart[lang])
    markup = show_return_lang_button(btn_restart, btn_cart)

    txt_add_cart = f"{my_dict.confirm_carts_msg[lang]}\n{wine['title']} {wine['collection']}"
    bot.send_message(user_id, text=txt_add_cart, reply_markup=markup)


def send_cart_message(user_id):
    step = users[user_id]['step']
    lang = users[user_id]['lang']
    wines = users_cart[user_id]
    text_message = [['Ваша корзина: ', 'Your cart: '][lang]]

    for i, w in enumerate(wines, 1):
        title = f"{w['title']} {w['collection']}" if w['collection'] is not None else f"{w['title']}"
        point = f"<b>{i}. {title}, {w['price']}0 €</b>"
        if 'amount' in w:
            point += f"<b> - {w['amount']}{['шт', 'qty'][lang]}</b>"
            if w['amount'] == 0:
                point = f"<s>{point}</s>"
        short_description = f"\n<i>{w['wtype'].capitalize()} {w['sugar']}</i>"
        if w['wstyle'] is not None:
            short_description = f"\n<i>{w['wtype'].capitalize()} {w['wstyle']} {w['sugar']}</i>"

        point += short_description
        text_message.append(point)

    if step == 9:
        bot.send_message(user_id,
                         text=my_dict.wine_cart_msg[lang], parse_mode='HTML')
        bot.send_message(user_id,
                         text=my_dict.delivery_price_msg[lang])

    # Показываем кнопки Начать заново и Выбор языка
    btn = types.KeyboardButton(text=my_dict.restart_button[lang])
    markup = show_return_lang_button(btn)

    bot.send_message(user_id,
                     text='\n\n'.join(text_message), parse_mode='HTML', reply_markup=markup)

    if step == 10:
        cart_amount = round(sum([w['price'] * w['amount'] for w in wines]), 1)
        del_flag = int(cart_amount < 30)
        delivery = ['0€', '5€'][del_flag]
        total = cart_amount + (0, 5)[del_flag]
        users_cart[user_id].append({'delivery': ('n', 'y')[del_flag]})

        txt = f"{my_dict.cart_summary_msg[lang]} <b>{cart_amount}0€</b>\n" + \
              f"{['Доставка:', 'Delivery:'][lang]} <b>{delivery}</b>\n" + \
              f"{['Итого:', 'Total:'][lang]} <b>{total}0€</b>"

        markup_inline = types.InlineKeyboardMarkup(row_width=1)
        order_button = types.InlineKeyboardButton(my_dict.order_button[lang], callback_data='order')
        markup_inline.add(order_button)
        bot.send_message(user_id, text=txt, parse_mode='HTML', reply_markup=markup_inline)
        bot.send_message(user_id, text=my_dict.edit_qty_msg[lang], parse_mode='HTML')


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


def new_start(user_id):
    lang = users[user_id]['lang']

    bot.send_sticker(user_id, my_dict.sticker_id_dikaprio)
    bot.send_message(user_id, text=my_dict.new_start_msg[lang])

    # add order to the database
    t = threading.Thread(target=add_to_db_carts, args=(user_id, users_cart[user_id]))
    t.start()

    # delete unnecessary info
    del users[user_id]['wine_cart']
    del users_cart[user_id]

    print('Ordering!!!')
    print_test()

    # set step to 1
    users[user_id]['step'] = 1


def confirm_ordering(user_id):
    lang = users[user_id]['lang']

    # send message to the customer that order has been made
    order_id = get_orderid()
    users_cart[user_id].append({'order_id': order_id})
    txt = f"{['# заказа: ', '# order: '][lang]}<b>{order_id}</b>\n" + my_dict.ordering_confirm_msg[lang]
    bot.send_message(user_id, text=txt, parse_mode='HTML')

    # send message to employees that order has been made

    t = threading.Thread(target=sendmsg, args=(users_cart.get(user_id),))
    t.start()


    return new_start(user_id)


def check_address(user_id):
    check_exist_address(user_id)


def add_data_to_order(user_id, data):
    step = users[user_id]['step']
    lang = users[user_id]['lang']
    try:
        users_cart[user_id]
        if step == 11:
            # users_cart[user_id] = check_zero(user_id)
            zip_code = get_address(data)
            users_cart[user_id].append({'zip_code': zip_code})
            users_cart[user_id].append({'address': data})
        elif step == 12:
            data = get_phone(data)
            if not data:
                return bot.send_message(user_id, text=['Неверный ввод', 'Wrong data'][lang])
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
        bot.send_message(user_id, text=my_dict.ordering_address_msg[lang], parse_mode='HTML')
    elif step == 12:
        bot.send_message(user_id, text=my_dict.ordering_phone_msg[lang], parse_mode='HTML')
    elif step == 13:
        bot.send_message(user_id, text=my_dict.ordering_name[lang], parse_mode='HTML')


def check_zero(user_id):
    try:
        users_cart[user_id][:-1] = [wine for wine in users_cart[user_id][:-1] if wine['amount'] > 0]
        users[user_id]['wine_cart'] = set([wine['wine_id'] for wine in users_cart[user_id][:-1]])
    except:

        return []

    if not users[user_id]['wine_cart']:
        users_cart[user_id] = []

    return users_cart[user_id]


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
            intro_message(user_id)
            add_to_db_customers(user_id, users[user_id]['lang'])
            show_menu_step(user_id)

        elif message.text == '🇬🇧 English':
            users[user_id]['lang'] = 1
            intro_message(user_id)
            add_to_db_customers(user_id, users[user_id]['lang'])
            show_menu_step(user_id)

        elif message.text in my_dict.return_button:
            show_language_selection(user_id)

        elif message.text in my_dict.restart_button:
            users_wine.pop(user_id, None)
            restart_choose_wine(user_id)

        elif message.text in my_dict.confirm_button:
            try:
                users[user_id]['price']

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
            lang = users[user_id]['lang']
            users_wine.pop(user_id, None)
            cart_wineids = list(map(int, users[user_id]['wine_cart']))
            list_for_cart = get_description(cart_wineids, user_id, lang=lang, complete=False)
            users_cart.update(list_for_cart)
            send_cart_message(user_id)

        else:
            if step == 9 or step == 10:
                get_amount(user_id, message.text)
            elif step == 11:
                contact_data = message.text
                add_data_to_order(user_id, contact_data)
                ordering_address(user_id)
            elif step == 12:
                contact_data = message.text
                add_data_to_order(user_id, contact_data)
                ordering_address(user_id)
            elif step == 13:
                contact_data = message.text
                add_data_to_order(user_id, contact_data)
                confirm_ordering(user_id)


@bot.callback_query_handler(func=lambda call: True)
def get_call(call):
    print_test()
    user_id = call.message.chat.id
    step = users.setdefault(user_id, {'step': 0})['step']

    if step < 1:
        show_language_selection(user_id)

    else:

        try:
            lang = users[user_id]['lang']
        except KeyError:
            return show_language_selection(user_id)

        # check wine type
        if call.data in my_dict.terms['wtype']:
            users[user_id]['wtype'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wtype'][users[user_id]['wtype']][lang]}")

            if call.data in ('rose', 'fortified'):
                users[user_id]['step'] = 4

            elif call.data == 'sparkling':
                users[user_id]['step'] = 3

            else:
                users[user_id]['step'] = 2

            show_menu_step(user_id)

        # check wine style
        elif call.data in my_dict.terms['wstyle']:
            users[user_id]['wstyle'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['wstyle'][users[user_id]['wstyle']][lang]}")

            # КОСТЫЛЬ!!! Разобраться!!!
            # users[user_id]['wtype'] = users[user_id]['wstyle'].split('_')[-1]

            users[user_id]['step'] = 3
            if users[user_id]['wtype'] == 'orange':
                users[user_id]['step'] = 4
            elif users[user_id]['wtype'] == 'fortified':
                users[user_id]['step'] = 6
            show_menu_step(user_id)

        # check sugar in wine
        elif call.data in my_dict.terms['sugar']:
            users[user_id]['sugar'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['sugar'][users[user_id]['sugar']][lang]}")

            users[user_id]['step'] = 4
            show_menu_step(user_id)

        # check country
        elif call.data in my_dict.terms['country']:
            users[user_id]['country'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['country'][users[user_id]['country']][lang]}")

            # НЕ ЗАБЫТЬ УДАЛИТЬ ЛИШНЕЕ УСЛОВИЕ or (users[user_id].get('sugar', None) == 'semi_dry'
            if users[user_id].get('wtype', None) in ('red', 'white') \
                    and users[user_id].get('sugar', None) == 'dry':
                # or (users[user_id].get('sugar', None) == 'semi_dry'
                # and users[user_id].get('wtype', None) == 'white'):
                users[user_id]['step'] = 5

            else:
                users[user_id]['step'] = 6

            show_menu_step(user_id)
        # check next step
        elif call.data in my_dict.terms['next_step']:
            users[user_id]['step'] = 52
            if call.data == 'step_grape':
                users[user_id]['step'] = 51
            show_menu_step(user_id)

        # check grapes
        elif call.data in my_dict.terms['grape']:
            users[user_id]['grape'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['grape'][users[user_id]['grape']][lang]}")

            users[user_id]['step'] = 6
            show_menu_step(user_id)

        # check regions
        elif call.data in my_dict.terms['region']:
            users[user_id]['region'] = call.data
            bot.send_message(user_id,
                             text=f"{['Вы выбрали: ', 'You choose: '][lang]}" +
                                  f"{my_dict.terms['region'][users[user_id]['region']][lang]}")

            users[user_id]['step'] = 6
            show_menu_step(user_id)

        # check skip option
        elif call.data == 'skip' and step in (5, 51, 52):
            users[user_id]['step'] = 6
            show_menu_step(user_id)

        # check price
        elif call.data in my_dict.terms['price']:
            users[user_id]['price'] = call.data

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

        elif call.data == 'offerme':
            show_wines(user_id)

        elif call.data == 'prev' and users_wine:
            users_wine[user_id][-1] = max(0, users_wine[user_id][-1] - 1)
            show_wines(user_id)
        elif call.data == 'next' and users_wine:
            users_wine[user_id][-1] = min(len(users_wine[user_id]) - 2, users_wine[user_id][-1] + 1)
            show_wines(user_id)

        elif call.data == 'cart' and users_wine:
            add_to_cart(user_id)

        # Если нажали инлайн-кнопку "Подтвердить количество"
        elif call.data == 'order':
            # Сделать проверку на количество в корзине и удалить вино с 0
            users_cart[user_id] = check_zero(user_id)
            if users_cart[user_id]:
                users[user_id]['step'] = 11
                bot.send_message(user_id, text=my_dict.confirm_quantity_msg[lang])
                check_address(user_id)
                bot.send_message(user_id, text=my_dict.ordering_msg[lang])
                ordering_address(user_id)
            else:
                users[user_id]['step'] = 1
                show_menu_step(user_id)


if __name__ == '__main__':
    users = {}
    bot.polling(none_stop=True, interval=0)
