dict_steps = {
    1: ('wtype', ('Тип вина: ', 'Wine type: ')),
    2: ('wstyle', ('Стиль: ', 'Style: ')),
    3: ('sugar', ('Сахар: ', 'Sugar: ')),
    4: ('country', ('Страна: ', 'Country: ')),
    5: ('grape', ('Сорт винограда/Регион: ', 'Grape/Region: ')),
    6: ('price', ('Цена: ', 'Price: '))
}

port_regions = (('Дуэйру', 'Алентежу', 'Винью Верде', 'Дао'),
                ('Douro', 'Alentejo', 'Vinho Verde', 'Dão'),
                ('douro', 'alentejo', 'vinho verde', 'dao'))

empty_grapes = (('Другой',), ('Other',), ('other',))

grapes_dict = {
        'douro': ('Дуэйру', 'Douro'),
        'alentejo': ('Алентежу', 'Alentejo'),
        'vinho verde': ('Винью Верде', 'Vinho Verde'),
        'dao': ('Дао', 'Dão'),
        'pinot noir': ('Пино Нуар', 'Pinot Noir'),
        'nebbiolo': ('Нибиола', 'Nebbiolo'),
        'sangiovese': ('Санджовезе', 'Sangiovese'),
        'garnacha': ('Гарнача', 'Garnacha'),
        'cabernet sauvignon': ('Каберне Совиньон', 'Cabernet Sauvignon'),
        'merlot': ('Мерло', 'Merlot'),
        'syrah': ('Сира', 'Syrah'),
        'sauvignon blanc': ('Совиньон Блан', 'Sauvignon Blanc'),
        'riesling': ('Рислинг', 'Riesling'),
        'alvarinho': ('Альвариньо', 'Alvarinho'),
        'gewurztraminer': ('Гевюрцтраминер', 'Gewürztraminer'),
        'muscat': ('Мускат', 'Muscat'),
        'chardonnay': ('Шардоне', 'Chardonnay'),
        'chenin blanc': ('Шенен Блан', 'Chenin Blanc'),
        'gamay': ('Гамэ', 'Gamay'),
        'cabernet franc': ('Каберне Фран', 'Cabernet Franc'),
        'côt': ('Кот (Мальбек)', 'Côt (Malbec)'),
        'tempranillo': ('Темпранильо', 'Tempranillo'),
        'mencia': ('Менсия', 'Mencia'),
        'grenache': ('Гренаш', 'Grenache'),
        'terrano': ('Террано', 'Terrano'),
        'grenache, syrah, mourvèdre': ('GSM-бленд', 'GSM-blend'),
        'malbec': ('Мальбек', 'Malbec'),
        'primitivo': ('Примитиво', 'Primitivo'),
        'barbera': ('Барбера', 'Barbera'),
        'blaufrankisch': ('Блауфренкиш', 'Blaufrankisch'),
        'loureiro': ('Лурейру', 'Loureiro'),
        'muscadet': ('Мускаде', 'Muscadet'),
        'trebbiano': ('Треббиано', 'Trebbiano'),
        'sylvaner': ('Сильванер', 'Sylvaner'),
        'pinot gris': ('Пино Грис', 'Pinot Gris'),
        'torrontés': ('Торронтес', 'Torrontés'),
        'verdicchio': ('Вердиккио', 'Verdicchio'),
        'other': ('Другой', 'Other')
    }

# при добавлении нового языка - добавить новое значение в каждый список
# при добавлении нового значения - добавить новую пару ключ: значение
terms = {
    'wtype': {
        'red': ('Красное', 'Red'),
        'white': ('Белое', 'White'),
        'rose': ('Розовое', 'Rose'),
        'orange': ('Оранж', 'Orange'),
        'sparkling': ('Игристое', 'Sparkling'),
        'fortified': ('Крепленое', 'Fortified')
    },
    'wstyle': {
        'light': ('Легкотельное', 'Light-bodied'),
        'medium': ('Среднетелое', 'Medium-bodied'),
        'full': ('Полнотелое', 'Full-bodied')
    },
    'sugar': {
        'brut': ('Брют', 'Brut'),
        'dry': ('Сухое', 'Dry'),
        'semi_sweet': ('Полусладкое', 'Semi-sweet')
    },
    'country': {
        'portugal': ('Португалия', 'Portugal'),
        'italy': ('Италия', 'Italy'),
        'spain': ('Испания', 'Spain'),
        'georgia': ('Грузия', 'Georgia'),
        'france': ('Франция', 'France'),
        'germany': ('Германия', 'Germany'),
        'others': ('Другие', 'Others')
    },
    'grape': grapes_dict,
    'price': {
        '0_10': ('До 10 евро', 'Up to 10 euros'),
        '10_15': ('От 10 до 15 евро', 'Between €10 and €15'),
        '15_20': ('От 15 до 20 евро', 'Between €15 and €20'),
        '20_30': ('От 20 до 30 евро', 'Between €20 and €30'),
        '30_10000': ('Более 30 евро', 'More than €30')
    }
}

# при добавлении нового типа - добавить в каждый список
# при добавлении нового языка - добавить новый список в предпоследний индекс
# в последнем списке хранятся значения, которые будут передаваться по нажатию кнопки
dict_categories = {
    'wtype': (('🍷 Красное', '🥂 Белое', '🌹 Розовое', '🍊 Оранж', '🍾 Игристое', '💪 Крепленое'),
              ('🍷 Red', '🥂 White', '🌹 Rose', '🍊 Orange', '🍾 Sparkling', '💪 Fortified'),
              ('red', 'white', 'rose', 'orange', 'sparkling', 'fortified')),
    'wstyle': (('Легкотелое', 'Среднетелое', 'Полнотелое'),
               ('Light-bodied', 'Medium-bodied', 'Full-bodied'),
               ('light', 'medium', 'full')),
    'sugar': (('Брют', 'Сухое', 'Полусладкое'),
              ('Brut', 'Dry', 'Semi-sweet'),
              ('brut', 'dry', 'semi_sweet')),
    'country': {
        'red': (('Португалия', 'Франция', 'Италия', 'Испания', 'Грузия', 'Другие'),
                ('Portugal', 'France', 'Italy', 'Spain', 'Georgia', 'Others'),
                ('portugal', 'france', 'italy', 'spain', 'georgia', 'others')),
        'white': (('Португалия', 'Франция', 'Италия', 'Испания', 'Германия', 'Другие'),
                  ('Portugal', 'France', 'Italy', 'Spain', 'Germany', 'Others'),
                  ('portugal', 'france', 'italy', 'spain', 'germany', 'others')),
        'rose': (('Португалия', 'Франция', 'Италия', 'Испания', 'Другие'),
                 ('Portugal', 'France', 'Italy', 'Spain', 'Others'),
                 ('portugal', 'france', 'italy', 'spain', 'others')),
        'orange': (('Португалия', 'Италия', 'Грузия', 'Другие'),
                   ('Portugal', 'Italy', 'Georgia', 'Others'),
                   ('portugal', 'italy', 'georgia', 'others')),
        'sparkling': (('Португалия', 'Франция', 'Италия', 'Другие'),
                      ('Portugal', 'France', 'Italy', 'Others'),
                      ('portugal', 'france', 'italy', 'others')),
        'fortified': (('Португалия', 'Испания', 'Другие'),
                      ('Portugal', 'Spain', 'Others'),
                      ('portugal', 'spain', 'others'))
    },
    'grape': {
        'red': {
            'light': {
                'portugal': empty_grapes,
                'france': (('Пино Нуар', 'Гамэ', 'Другой'),
                           ('Pinot Noir', 'Gamay', 'Other'),
                           ('pinot noir', 'gamay', 'other')),
                'spain': empty_grapes,
                'italy': empty_grapes,
                'georgia': empty_grapes,
                'others': empty_grapes
            },
            'medium': {
                'portugal': empty_grapes,
                'france': (('Каберне Фран', 'Сира', 'Кот (Мальбек)', 'Другой'),
                           ('Cabernet Franc', 'Syrah', 'Côt (Malbec)', 'Other'),
                           ('cabernet franc', 'syrah', 'côt', 'other')),
                'spain': (('Темпранильо', 'Менсия', 'Гренаш', 'Другой'),
                          ('Tempranillo', 'Mencia', 'Grenache', 'Other'),
                          ('tempranillo', 'mencia', 'grenache', 'other')),
                'italy': (('Санджовезе', 'Неббиоло', 'Террано', 'Другой'),
                          ('Sangiovese', 'Nebbiolo', 'Terrano', 'Other'),
                          ('sangiovese', 'nebbiolo', 'terrano', 'other')),
                'georgia': empty_grapes,
                'others': empty_grapes
            },
            'full': {
                'portugal': empty_grapes,
                'france': (('Сира', 'GSM-бленд', 'Мальбек', 'Другой'),
                           ('Syrah', 'GSM-blend', 'Malbec', 'Other'),
                           ('syrah', 'grenache, syrah, mourvèdre', 'malbec', 'other')),
                'spain': (('Темпранильо', 'Другой'),
                          ('Tempranillo', 'Other'),
                          ('tempranillo', 'other')),
                'italy': (('Неббиоло', 'Примитиво', 'Барбера', 'Другой'),
                          ('Nebbiolo', 'Primitivo', 'Barbera', 'Other'),
                          ('nebbiolo', 'primitivo', 'barbera', 'other')),
                'georgia': empty_grapes,
                'others': (('Мальбек', 'Каберне Совиньон', 'Блауфренкиш', 'Другой'),
                           ('Malbec', 'Cabernet Sauvignon', 'Blaufrankisch', 'Other'),
                           ('malbec', 'cabernet sauvignon', 'blaufrankisch', 'other'))
            }

        },
        'white': {
            'light': {
                'portugal': (('Лурейру', 'Алваринью', 'Другой'),
                             ('Loureiro', 'Alvarinho', 'Other'),
                             ('loureiro', 'alvarinho', 'other')),
                'france': (('Шардоне', 'Мускаде', 'Шенен Блан', 'Другой'),
                           ('Chardonnay', 'Muscadet', 'Chenin Blanc', 'Other'),
                           ('chardonnay', 'muscadet', 'chenin blanc', 'other')),
                'spain': (('Албаринью', 'Другой'),
                          ('Alvarinho', 'Other'),
                          ('alvarinho', 'other')),
                'italy': (('Треббиано', 'Другой'),
                          ('Trebbiano', 'Other'),
                          ('trebbiano', 'other')),
                'georgia': empty_grapes,
                'others': (('Рислинг', 'Сильванер', 'Другой'),
                           ('Riesling', 'Sylvaner', 'Other'),
                           ('riesling', 'sylvaner', 'other'))
            },
            'medium': {
                'portugal': empty_grapes,
                'france': (('Шенен Блан', 'Рислинг', 'Шардоне', 'Пино Грис', 'Другой'),
                           ('Chenin Blanc', 'Riesling', 'Chardonnay', 'Pinot Gris', 'Other'),
                           ('chenin blanc', 'riesling', 'chardonnay', 'pinot gris', 'other')),
                'spain': (('Торронтес', 'Албаринью', 'Другой'),
                          ('Torrontés', 'Albarinho', 'Other'),
                          ('torrontés', 'alvarinho', 'other')),
                'italy': (('Вердиккио', 'Другой'),
                          ('Verdicchio', 'Other'),
                          ('verdicchio', 'other')),
                'georgia': empty_grapes,
                'others': empty_grapes
            },
            'full': {
                'portugal': empty_grapes,
                'france': (('Шардоне', 'Другой'),
                           ('Chardonnay', 'Other'),
                           ('chardonnay', 'other')),
                'spain': empty_grapes,
                'italy': empty_grapes,
                'georgia': empty_grapes,
                'others': empty_grapes
            }
        }
    },
    'price': (('До 10 евро', 'От 10 до 15 евро', 'От 15 до 20 евро', 'От 20 до 30 евро', 'Более 30 евро'),
              ('Up to 10 euros', 'Between €10 and €15', 'Between €15 and €20', 'Between €20 and €30', 'More than €30'),
              ('0_10', '10_15', '15_20', '20_30', '30_10000'))
}

### СООБЩЕНИЯ И КНОПКИ ################################################################################################

choose_lang = '🇷🇺 Выберите язык\n🇬🇧 Choose your language'

intro_message = ['''
Добро пожаловать!!!
Я виртуальный ассистент, Awiner 🦸
Готов помочь вам в выборе вина!
''',
                 '''
Welcome!!!
I am Awiner's virtual assistant 🦸
Ready to help you with your wine selection!
''']

help_message = ['''
Вам будет предложено поочердно выбрать из таких критериев вина, как:
тип, стиль, содержание сахара, страна, сорт винограда и цена.
Давайте начнем!
''',
                '''
You will be asked to take turns selecting a wine based on criteria such as:
type, style, sugar content, country, grape variety and price.
Let's get started!
''']

ai_message = ['''
Или вы можете написать мне сообщение о ваших предпочтениях
И я постараюсь сделать подбор
!!!ПОКА НЕ РАБОТАЕТ!!!
''',
              '''
Or you can write me a message about your preferences.
And I will try to make a choice.
!!!NOT WORKING YET!!!
''']

return_button = '🔙 🇷🇺 RU / 🇬🇧 GB (US)'

dict_messages = {
    1: ['Какой тип вина вы предпочитаете?',
        'What type of wine do you prefer?'],
    2: [
'''Теперь давайте выберем стиль вина.
Вы предпочли бы легкое и освежающее вино или полнотелое и насыщенное?''',
'''Now, let's choose the wine style.
Would you prefer a light and refreshing wine or a full-bodied and rich one?'''],
    3: ['Какое содержание сахара?',
        'How much sugar content?'],
    4: ["Давайте выберем страну!",
        "Let's choose a country!"],
    5: ["Вы предпочитаете какие-то конкретные сорта винограда?\n"
        "*Этот шаг можно пропустить*",
        "Do you prefer any particular grape varieties?\n"
        "*This step can be skipped*"],
    6: ["Давайте определимся с ценой!",
        "Let's set a price!"]
}

skip_text = ['Пропустить!', 'Skip!']

wine_suggest_message = ['Теперь мне достаточно данных для предложения вина!',
                        'Now I have enough data for a wine suggestion!']


confirm_fltr_msg = ['Если все верно - жмите кнопку: Подтвердить!\n\nЕсли сомневаетесь: Начать заново!',
                    'If everything is correct - click: Confirm!\n\nIf in doubt: Start again!']

confirm_button = ['Подтвердить!',
                  'Confirm!']

restart_button = ['Начать заново!', 'Start again!']

restart_text = ["Давайте сделаем еще один выбор!",
                "Let's make another choice!"]

show_wines_msg = ['Согласно вашему запросу:',
                  'According to your request:']

empty_res_msg = ['Ничего не найдено!', 'Nothing found!']

fwd_button = ['Вперед', 'Next']
cart_button = ['В корзину!', 'Add to cart']
bwd_button = ['Назад', 'Previous']

error_msg = ['Что-то не так!\nДавайте начнем сначала!',
             "Something's gone wrong!\nLet's start again!"]

btn_cart = ['Корзина', 'Cart']

mandatory_cats = ('wstyle', 'sugar', 'country', 'price')
mandatory_cats_rose = ('country', 'price')
mandatory_cats_orange = ('wstyle', 'country', 'price')
mandatory_cats_sparkling = ('sugar', 'country', 'price')
mandatory_cats_fortified = ('wstyle', 'price')

more_cats_msg = ['Не хватает данных!\nНачнем сначала)', "Not enough data! Let's start over)"]

confirm_carts_msg = ['Добавлено в корзину:', 'Added to cart:']

wine_cart_msg = ['Введите через пробел количество в поле для сообщений\n'
                 '0 - если хотите удалить какое-то вино\n'
                 'Пример для корзины из 4х вин: 1 3 2 2',
                 'Enter the quantity using SPACE in the message box\n'
                 '0 - if you want to remove a wine\n'
                 'Example for a basket of 4 wines: 1 3 2 2']

error_quant_msg = ['!!!Указано неверное количество!!!\nИзменение не выполнено\nВведите еще раз',
                   '!!!Incorrect quantity!!!\nChange has not been made\nEnter again']

delivery_price_msg = ['Стоимость доставки (Лиссабон-Кашкайш):\n'
                      'Сумма заказа <30€ = 5€\n'
                      'Сумма заказа >30€ = Бесплатно',
                      'Delivery charges (Lisbon-Cascais):\n'
                      'Order amount <30€ = 5€\n'
                      'Order amount >30€ = Free']

cart_summary_msg = ['Ваш заказ на сумму:', 'Your order is:']

order_button = ['Подтвердить количество', 'Confirm quantity']
edit_qty_msg = ['Для редактирования количества введите в строку сообщения новые значения',
                'To edit the quantity, enter new values in the message line']

ordering_msg = ['Для завершения оформления вам потребуется ввести:\n'
                '- адрес\n- телефон\n -имя',
                'You will need to enter the following to complete the application\n'
                '- address\n- telephone number\n-name']

ordering_address_msg = ['Введите адрес доставки\nПо возможности укажите почтовый индекс',
                        'Enter the delivery address\nPlease enter the postcode if possible']

ordering_phone_msg = ['Укажите номер телефона (6-12 цифр)',
                      'Enter local phone number (6-12 digits)']

ordering_name = ['Напишите, пожалуйста, ваше имя',
                      'Please write your name']

ordering_confirm_msg = ['Спасибо за ваш заказ!\n'
                        'В ближайшее время мы свяжемся с вами для уточнения деталей доставки',
                        'Thank you for your order!\n'
                        'We will contact you shortly for delivery details']