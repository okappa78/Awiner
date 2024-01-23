import psycopg2
from psycopg2.extensions import register_adapter, AsIs
from datetime import datetime
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
db_uri = os.getenv('DB_URI')

max_length_address = 100
max_length_customer_name = 30

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def add_to_db_customers(user_id, lang):
    # connect to database
    conn = psycopg2.connect(db_uri, sslmode='require')
    cursor = conn.cursor()

    # create table if not exist
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id SERIAL PRIMARY KEY,
                    start_time TIMESTAMP,
                    user_id BIGINT,
                    customer_name VARCHAR(30),
                    zip_code VARCHAR(10),
                    address VARCHAR(100),
                    phone VARCHAR(15),
                    lang INTEGER
                )
            ''')

    # check if user exist in table
    cursor.execute("SELECT * FROM customers WHERE user_id=%s", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.execute('''UPDATE customers SET lang=%s WHERE user_id=%s''', (lang, user_id))
    else:
        timestamp = get_timestamp()
        cursor.execute('''INSERT INTO customers (start_time, user_id, lang)
                                          VALUES (%s, %s, %s)''', (timestamp, user_id, lang))

    # committing the changes
    conn.commit()
    # close connection
    conn.close()
    print('new customer was added')


def add_to_db_filters(user_id, mydict):
    # Подключение к базе данных
    conn = psycopg2.connect(db_uri, sslmode='require')
    cursor = conn.cursor()
    
    # Создание таблицы, если она не существует
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS filters (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP,
                user_id BIGINT,
                wine_type VARCHAR(15),
                wine_style VARCHAR(15),
                wine_sugar VARCHAR(15),
                wine_country VARCHAR(30),
                wine_grape VARCHAR(50),
                wine_price VARCHAR(10),
                lang INTEGER,
                wine_region VARCHAR(50)
            )
        ''')

    fieldnames = ('wtype', 'wstyle', 'sugar', 'country', 'grape', 'price', 'lang', 'region')
    filters = [mydict.get(key, None) for key in fieldnames]
    timestamp = get_timestamp()
    add_values = (timestamp, user_id, *filters)

    register_adapter(np.int64, AsIs)
    cursor.execute('''INSERT INTO filters (timestamp, user_id, wine_type, wine_style, wine_sugar,
                                                  wine_country, wine_grape, wine_price, lang, wine_region)
                                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', add_values)
    # Committing the changes
    conn.commit()
    # Закрытие соединения
    conn.close()


def add_to_db_carts(user_id, mylst):
    # Подключение к базе данных
    conn = psycopg2.connect(db_uri, sslmode='require')
    cursor = conn.cursor()
    
    # Создание таблицы, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carts (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            order_id VARCHAR(10),
            user_id BIGINT,
            wine_id INTEGER,
            title VARCHAR(50),
            price DOUBLE PRECISION,
            amount INTEGER,
            delivery VARCHAR(5),
            zip_code VARCHAR(10),
            address VARCHAR(100),
            phone VARCHAR(15),
            customer_name VARCHAR(30)
        )
    ''')

    # Обрезаем лишние символы в адресе и имени
    mylst[-3]['address'] = mylst[-3]['address'][:max_length_address]
    mylst[-1]['customer_name'] = mylst[-1]['customer_name'][:max_length_customer_name]

    # Преобразовываем список [{вина} + {контактные данны}] в список [{вино + контактные данные}]
    len_dict = len(mylst) - 6
    [mylst[i].update(contact) for contact in mylst[-6:] for i in range(len_dict)]
    dict_userid = {'user_id': user_id, 'timestamp': get_timestamp()}
    [wine.update(dict_userid) for wine in mylst]
    mylst = mylst[:-6]

    fieldnames = ('timestamp', 'order_id', 'user_id', 'wine_id', 'title',
                  'price', 'amount', 'delivery', 'zip_code', 'address', 'phone', 'customer_name')
    # Получаем данные в виде списка списков
    lst_values = [tuple([wine.get(key, None) for key in fieldnames]) for wine in mylst]

    register_adapter(np.int64, AsIs)
    for values in lst_values:
        cursor.execute('''INSERT INTO carts (timestamp, order_id, user_id, wine_id, title, price,
                                                  amount, delivery, zip_code, address, phone, customer_name)
                                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', values)

    # Committing the changes
    conn.commit()
    # Закрытие соединения
    conn.close()


def add_to_db_address(user_id, contact_data_lst):
    zip_code = contact_data_lst[0]['zip_code']
    address = contact_data_lst[1]['address'][:max_length_address]
    phone = contact_data_lst[2]['phone']
    customer_name = contact_data_lst[3]['customer_name'][:max_length_customer_name]

    # connect to database
    conn = psycopg2.connect(db_uri, sslmode='require')
    cursor = conn.cursor()

    cursor.execute('''UPDATE customers
                      SET customer_name=%s, zip_code=%s, address=%s, phone=%s
                      WHERE user_id=%s''', (customer_name, zip_code, address, phone, user_id))

    # committing the changes
    conn.commit()
    # close connection
    conn.close()
    print('new address was added')
