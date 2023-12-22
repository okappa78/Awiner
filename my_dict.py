dict_steps = {
    1: ('wtype', ('Тип вина: ', 'Wine type: ')),
    2: ('wstyle', ('Стиль: ', 'Style: ')),
    3: ('sugar', ('Сахар: ', 'Sugar: ')),
    4: ('country', ('Страна: ', 'Country: ')),
    5: ('next_step', ('Следующий шаг: ', 'Next step: ')),
    51: ('grape', ('Сорт винограда: ', 'Grape: ')),
    52: ('region', ('Регион: ', 'Region: ')),
    6: ('price', ('Цена: ', 'Price: '))
}

empty_grapes = (('Другой',), ('Other',), ('other',))

regions_dict = {
        'abruzzo': ('Абруццо', 'Abruzzo'),
        'alentejo': ('Алентежу', 'Alentejo'),
        'alsace': ('Эльзас', 'Alsace'),
        'alto adige': ('Альто-Адидже', 'Alto Adige'),
        'bairrada': ('Байррада', 'Bairrada'),
        'bordeaux': ('Бордо', 'Bordeaux'),
        'bourgogne': ('Бургундия', 'Bourgogne'),
        'canarias': ('Канарские о-ва', 'Canarias'),
        'dão': ('Дао', 'Dão'),
        'douro': ('Дору', 'Douro'),
        'galicia': ('Галисия', 'Galicia'),
        'lisboa': ('Лиссабон', 'Lisboa'),
        'loire': ('Луара', 'Loire'),
        'piemonte': ('Пьемонт', 'Piemonte'),
        'puglia': ('Апулия', 'Puglia'),
        'rhône': ('Рона', 'Rhône'),
        'ribera del duero': ('Рибера-дель-Дуэро', 'Ribera Del Duero'),
        'rioja': ('Риоха', 'Rioja'),
        'sicilia': ('Сицилия', 'Sicilia'),
        'toscana': ('Тоскана', 'Toscana'),
        'veneto': ('Венето', 'Veneto'),
        'vinho verde': ('Винью Верде', 'Vinho Verde')
}


grapes_dict = {
    'airén': ('Айрен', 'Airén'),
    'albariño': ('Альбариньо', 'Albariño'),
    'alvarinho': ('Альвариньо', 'Alvarinho'),
    'barbera': ('Барбера', 'Barbera'),
    'blaufrankisch': ('Блауфренкиш', 'Blaufrankisch'),
    'cabernet franc': ('Каберне Фран', 'Cabernet Franc'),
    'cabernet sauvignon': ('Каберне Совиньон', 'Cabernet Sauvignon'),
    'chenin blanc': ('Шенен Блан', 'Chenin Blanc'),
    'chardonnay': ('Шардоне', 'Chardonnay'),
    'côt': ('Кот (Мальбек)', 'Côt (Malbec)'),
    'fiano di avellino': ('Фиано ди Авеллино', 'Fiano di Avellino'),
    'gamay': ('Гамэ', 'Gamay'),
    'garnacha': ('Гарнача', 'Garnacha'),
    'garnacha blanca': ('Гарнача Бланка', 'Garnacha Blanca'),
    'gewurztraminer': ('Гевюрцтраминер', 'Gewürztraminer'),
    'glera': ('Глера', 'Glera'),
    'grenache': ('Гренаш', 'Grenache'),
    'grenache blanc': ('Гренаш Блан', 'Grenache Blanc'),
    'grenache, syrah, mourvèdre': ('GSM-бленд', 'GSM-blend'),
    'loureiro': ('Лурейру', 'Loureiro'),
    'malbec': ('Мальбек', 'Malbec'),
    'merlot': ('Мерло', 'Merlot'),
    'mencia': ('Менсия', 'Mencia'),
    'moscato ': ('Москато', 'Moscato'),
    'muscadet': ('Мускаде', 'Muscadet'),
    'muscat': ('Мускат', 'Muscat'),
    'nebbiolo': ('Нибиола', 'Nebbiolo'),
    'other': ('Другой', 'Other'),
    'pinot bianco': ('Пино Бьянко', 'Pinot Bianco'),
    'pinot grigio': ('Пино Гриджио', 'Pinot Grigio'),
    'pinot gris': ('Пино Грис', 'Pinot Gris'),
    'pinot noir': ('Пино Нуар', 'Pinot Noir'),
    'primitivo': ('Примитиво', 'Primitivo'),
    'riesling': ('Рислинг', 'Riesling'),
    'sangiovese': ('Санджовезе', 'Sangiovese'),
    'sauvignon blanc': ('Совиньон Блан', 'Sauvignon Blanc'),
    'syrah': ('Сира', 'Syrah'),
    'sylvaner': ('Сильванер', 'Sylvaner'),
    'tempranillo': ('Темпранильо', 'Tempranillo'),
    'terrano': ('Террано', 'Terrano'),
    'torrontés': ('Торронтес', 'Torrontés'),
    'trebbiano': ('Треббиано', 'Trebbiano'),
    'verdejo': ('Вердехо', 'Verdejo'),
    'verdicchio': ('Вердиккио', 'Verdicchio'),
    'vermentino': ('Верментино', 'Vermentino'),
    'viognier': ('Вионье́', 'Viognier'),
    'viura': ('Виура', 'Viura')
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
        'medium_sweet': ('Полусладкое', 'Semi-sweet')
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
    'next_step': {
        'step_grape': ('Виноград', 'Grape'),
        'step_region': ('Регион', 'Region')
    },
    'grape': grapes_dict,
    'region': regions_dict,
    'price': {
        '0_15': ('До 15 евро', 'Up to €15'),
        '15_25': ('От 15 до 25 евро', 'Between €15 and €25'),
        '25_35': ('От 25 до 35 евро', 'Between €25 and €35'),
        '35_50': ('От 35 до 50 евро', 'Between €35 and €50'),
        '50_10000': ('Более 50 евро', 'More than €50')
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
              ('brut', 'dry', 'medium_sweet')),
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
    'next_step': (('Виноград', 'Регион'),
                  ('Grape', 'Region'),
                  ('step_grape', 'step_region')),
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
                'france': (('Шардоне', 'Совиньон Блан', 'Гренаш Блан', 'Мускаде', 'Другой'),
                           ('Chardonnay', 'Sauvignon Blanc', 'Grenache Blanc', 'Muscadet', 'Other'),
                           ('chardonnay', 'sauvignon blanc', 'grenache blanc', 'muscadet', 'other')),
                'spain': (('Альбариньо', 'Вердехо', 'Другой'),
                          ('Albariño', 'Verdejo', 'Other'),
                          ('albariño', 'verdejo', 'other')),
                'italy': (('Глера', 'Москато', 'Пино Гриджио', 'Треббиано', 'Другой'),
                          ('Glera', 'Moscato', 'Pinot Grigio', 'Trebbiano', 'Other'),
                          ('glera', 'moscato', 'pinot grigio', 'trebbiano', 'other')),
                'georgia': empty_grapes,
                'others': (('Рислинг', 'Сильванер', 'Другой'),
                           ('Riesling', 'Sylvaner', 'Other'),
                           ('riesling', 'sylvaner', 'other'))
            },
            'medium': {
                'portugal': empty_grapes,
                'france': (('Шардоне', 'Шенен Блан', 'Рислинг', 'Вионье́', 'Другой'),
                           ('Chardonnay', 'Chenin Blanc', 'Riesling', 'Viognier', 'Other'),
                           ('chardonnay', 'chenin blanc', 'riesling', 'viognier', 'other')),
                'spain': (('Айрен', 'Альбариньо', 'Торронтес', 'Виура', 'Другой'),
                          ('Airén', 'Albariño', 'Torrontés', 'Viura', 'Other'),
                          ('airén', 'albariño', 'torrontés', 'viura', 'other')),
                'italy': (('Шардоне', 'Пино Бьянко', 'Вердиккио', 'Верментино', 'Другой'),
                          ('Chardonnay', 'Pinot Bianco', 'Verdicchio', 'Vermentino', 'Other'),
                          ('chardonnay', 'pinot bianco', 'verdicchio', 'vermentino', 'other')),
                'georgia': empty_grapes,
                'others': empty_grapes
            },
            'full': {
                'portugal': empty_grapes,
                'france': (('Шардоне', 'Гевюрцтраминер', 'Рислинг', 'Вионье́', 'Другой'),
                           ('Chardonnay', 'Gewürztraminer', 'Riesling', 'Viognier', 'Other'),
                           ('chardonnay', 'gewurztraminer', 'riesling', 'viognier', 'other')),
                'spain': (('Альбариньо', 'Гарнача Бланка', 'Другой'),
                          ('Albariño', 'Garnacha Blanca', 'Other'),
                          ('albariño', 'garnacha blanca', 'other')),
                'italy': (('Фиано ди Авеллино', 'Вердиккио', 'Другой'),
                          ('Fiano di Avellino', 'Verdicchio', 'Other'),
                          ('fiano di avellino', 'verdicchio', 'other')),
                'georgia': empty_grapes,
                'others': empty_grapes
            }
        }
    },
    'region': {
        'red': {
                'portugal': (('Алентежу', 'Байррада', 'Дао', 'Дору', 'Лиссабон', 'Винью Верде', 'Другой'),
                             ('Alentejo', 'Bairrada', 'Dão', 'Douro', 'Lisboa', 'Vinho Verde', 'Other'),
                             ('alentejo', 'bairrada', 'dão', 'douro', 'lisboa', 'vinho verde', 'other')),
                'france': (('Бордо', 'Бургундия', 'Луара', 'Рона', 'Другой'),
                           ('Bordeaux', 'Bourgogne', 'Loire', 'Rhône', 'Other'),
                           ('bordeaux', 'bourgogne', 'loire', 'rhône', 'other')),
                'spain': (('Рибера-дель-Дуэро', 'Риоха', 'Другой'),
                          ('Ribera Del Duero', 'Rioja', 'Other'),
                          ('ribera del duero', 'rioja', 'other')),
                'italy': (('Пьемонт', 'Апулия', 'Тоскана', 'Венето', 'Другой'),
                          ('Piemonte', 'Puglia', 'Toscana', 'Veneto', 'Other'),
                          ('piemonte', 'puglia', 'toscana', 'veneto', 'other')),
                'georgia': empty_grapes,
                'others': empty_grapes
        },
        'white': {
                'portugal': (('Алентежу', 'Байррада', 'Дао', 'Дору', 'Лиссабон', 'Винью Верде', 'Другой'),
                             ('Alentejo', 'Bairrada', 'Dão', 'Douro', 'Lisboa', 'Vinho Verde', 'Other'),
                             ('alentejo', 'bairrada', 'dão', 'douro', 'lisboa', 'vinho verde', 'other')),
                'france': (('Эльзас', 'Бордо', 'Бургундия', 'Луара', 'Другой'),
                           ('Alsace', 'Bordeaux', 'Bourgogne', 'Loire', 'Other'),
                           ('alsace', 'bordeaux', 'bourgogne', 'loire', 'other')),
                'spain': (('Канарские о-ва', 'Галисия', 'Другой'),
                          ('Canarias', 'Galicia', 'Other'),
                          ('canarias', 'galicia', 'other')),
                'italy': (('Абруццо', 'Альто-Адидже', 'Сицилия', 'Тоскана', 'Другой'),
                          ('Abruzzo', 'Alto Adige', 'Sicilia', 'Toscana', 'Other'),
                          ('abruzzo', 'alto adige', 'sicilia', 'toscana', 'other')),
                'georgia': empty_grapes,
                'others': empty_grapes
        }
    },
    'price': (('До 15 евро', 'От 15 до 25 евро', 'От 25 до 35 евро', 'От 35 до 50 евро', 'Более 50 евро'),
              ('Up to 15 euros', 'Between €15 and €25', 'Between €25 and €35', 'Between €35 and €50', 'More than €50'),
              ('0_15', '15_25', '25_35', '35_50', '50_10000'))
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
    5: ["Вы выбираете вино по винограду или региону?\n"
        "*Эти шаги можно пропустить*",
        "Do you choose your wine by grape or region?\n"
        "*These steps can be skipped*"],
    51: ["Какие сорта винограда вы предпочитаете?\n"
        "*Этот шаг можно пропустить*",
        "What grape varieties do you prefer?\n"
        "*This step can be skipped*"],
    52: ["Какой регион вы предпочитаете?\n"
        "*Этот шаг можно пропустить*",
        "What region do you prefer?\n"
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

fwd_button = ['Следующее', 'Next']
cart_button = ['В корзину!', 'Add to cart']
bwd_button = ['Предыдущее', 'Previous']

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