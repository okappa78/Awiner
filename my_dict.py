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


#при добавлении нового языка - добавить новое значение в каждый список
#при добавлении нового значения - добавить новую пару ключ: значение
terms = {
    'wine_type': {
        'red': ('Красное', 'Red'),
        'white': ('Белое', 'White'),
        'rose': ('Розовое', 'Rose')
    },
    'wine_style': {
        'light_red': ('Легкое красное', 'Light red'),
        'full_red': ('Полнотелое красное', 'Full-bodied red'),
        'light_white': ('Легкое свежее', 'Light and fresh'),
        'full_white': ('Фруктовое ароматное', 'Fruity flavour')
    },
    'wine_sugar': {
        'dry': ('Сухое', 'Dry'),
        'semi_dry': ('Полусухое', 'Semi-dry'),
        'semi_sweet': ('Полусладкое', 'Semi-sweet')
    },
    'wine_country': {
        'portugal': ('Португалия', 'Portugal'),
        'import': ('Импорт', 'Import'),
        'provence': ('Прованс', 'Provence')
    },
    'wine_grape': {
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
        'albarino': ('Альвариньо', 'Albariño'),
        'gewurztraminer': ('Гевюрцтраминер', 'Gewürztraminer'),
        'muscat': ('Мускат', 'Muscat'),
        'chardonnay': ('Шардоне', 'Chardonnay'),
        'chenin blanc': ('Шенен Блан', 'Chenin Blanc')
    },
    'wine_price': {
        '0_10': ('До 10 евро', 'Up to 10 euros'),
        '10_15': ('От 10 до 15 евро', 'Between €10 and €15'),
        '15_20': ('От 15 до 20 евро', 'Between €15 and €20'),
        '20_30': ('От 20 до 30 евро', 'Between €20 and €30'),
        '30_1000': ('Более 30 евро', 'More than €30')
    }
}


dict_steps = {
    1: ['wine_type', ['Тип вина: ', 'Wine type: ']],
    2: ['wine_style', ['Стиль: ', 'Style: ']],
    3: ['wine_sugar', ['Сахар: ', 'Sugar: ']],
    4: ['wine_country', ['Тип вина: ', 'Country: ']],
    5: ['wine_grape', ['Сорт винограда/Регион: ', 'Grape/Region: ']],
    6: ['wine_price', ['Цена: ', 'Price: ']]
}

port_regions = (('Дуэйру', 'Алентежу', 'Винью Верде', 'Дао'),
                ('Douro', 'Alentejo', 'Vinho Verde', 'Dão'),
                ('douro', 'alentejo', 'vinho verde', 'dao'))

#при добавлении нового типа - добавить в каждый список
#при добавлении нового языка - добавить новый список в предпоследний индекс
#в последнем списке хранятся значения, которые будут передаваться по нажатию кнопки
dict_categories = {
    'wine_type': [['Красное', 'Белое', 'Розовое'],
                  ['Red', 'White', 'Rose'],
                  ['red', 'white', 'rose']],
    'wine_style': {
        'red': [['Легкое красное', 'Полнотелое красное'],
                ['Light red', 'Full-bodied red'],
                ['light_red', 'full_red']],
        'white': [['Легкое свежее', 'Фруктовое ароматное'],
                  ['Light and fresh', 'Fruity flavour'],
                  ['light_white', 'full_white']]
    },
    'wine_sugar': [['Сухое', 'Полусухое', 'Полусладкое'],
                   ['Dry', 'Semi-dry', 'Semi-sweet'],
                   ['dry', 'semi_dry', 'semi_sweet']],
    'wine_country': {
        'red': [['Португалия', 'Импорт'],
                ['Portugal', 'Import'],
                ['portugal', 'import']],
        'white': [['Португалия', 'Импорт'],
                  ['Portugal', 'Import'],
                  ['portugal', 'import']],
        'rose': [['Португалия', 'Прованс'],
                 ['Portugal', 'Provence'],
                 ['portugal', 'provence']]
    },
    'wine_grape': {
        'light_red': {
            'dry': {
                'portugal': port_regions,
                'import': [['Пино Нуар', 'Нибиола', 'Санджовезе', 'Гарнача'],
                          ['Pinot Noir', 'Nebbiolo', 'Sangiovese', 'Garnacha'],
                          ['pinot noir', 'nebbiolo', 'sangiovese', 'garnacha']]
            }
        },
        'full_red': {
            'dry': {
                'portugal': port_regions,
                'import': [['Каберне Совиньон', 'Мерло', 'Сира', 'Санджовезе', 'Гарнача'],
                           ['Cabernet Sauvignon', 'Merlot', 'Syrah', 'Sangiovese', 'Garnacha'],
                           ['cabernet sauvignon', 'merlot', 'syrah', 'sangiovese', 'garnacha']]
            }
        },
        'light_white': {
            'dry': {
                'portugal': port_regions,
                'import': [['Совиньон Блан', 'Рислинг', 'Альвариньо'],
                           ['Sauvignon Blanc', 'Riesling', 'Albariño'],
                           ['sauvignon blanc', 'riesling', 'albarino']]
            },
            'semi_dry': {
                'portugal': port_regions,
                'import': [['Рислинг', 'Гевюрцтраминер', 'Мускат'],
                           ['Riesling', 'Gewürztraminer', 'Muscat'],
                           ['riesling', 'gewurztraminer', 'muscat']]
            }
        },
        'full_white': {
            'dry':{
                'portugal': port_regions,
                'import': [['Шардоне', 'Шенен Блан'],
                           ['Chardonnay', 'Chenin Blanc'],
                           ['chardonnay', 'chenin blanc']]
            },
            'semi_dry': {
                'portugal': port_regions,
                'import': [['Рислинг', 'Гевюрцтраминер', 'Мускат'],
                           ['Riesling', 'Gewürztraminer', 'Muscat'],
                           ['riesling', 'gewurztraminer', 'muscat']]
            }
        }
    },
    'wine_price': [['До 10 евро', 'От 10 до 15 евро', 'От 15 до 20 евро', 'От 20 до 30 евро', 'Более 30 евро'],
                   ['Up to 10 euros', 'Between €10 and €15', 'Between €15 and €20', 'Between €20 and €30',
                    'More than €30'],
                   ['0_10', '10_15', '15_20', '20_30', '30_1000']]
}


dict_messages = {
    1: ['Какой тип вина вы предпочитаете?',
        'What type of wine do you prefer?'],
    2: [
'''Теперь давайте выберем стиль вина.
Вы предпочли бы легкое и освежающее вино или полнотелое и насыщенное?''',
'''Now, let's choose the wine style.
Would you prefer a light and refreshing wine or a full-bodied and rich one?'''],
    3: ['Сухое, полусухое, а может быть полусладкое?',
        'Dry, semi-dry, or perhaps semi-sweet?'],
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

error_msg = ['Что-то пошло не так!\nДавайте начнем сначала!',
             "Something's gone wrong!\nLet's start again!"]

btn_cart = ['Корзина', 'Cart']

mandatory_cats = ('wine_style', 'wine_sugar', 'wine_country', 'wine_price')
mandatory_cats_rose = ('wine_country', 'wine_price')

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