import os
import requests
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

import my_dict

load_dotenv()
db_uri = os.getenv('DB_URI')

countries = {k: v[-1][:-1] for k, v in my_dict.dict_categories['country'].items()}
grapes = {
        'red': {
            'light': {
                'france': ('pinot noir', 'gamay')
            },
            'medium': {
                'france': ('cabernet franc', 'syrah', 'côt'),
                'spain': ('tempranillo', 'mencia', 'grenache'),
                'italy': ('sangiovese', 'nebbiolo', 'terrano')
            },
            'full': {
                'france': ('syrah', 'grenache, syrah, mourvèdre', 'malbec'),
                'spain': ('tempranillo',),
                'italy': ('nebbiolo', 'primitivo', 'barbera'),
                'others': ('malbec', 'cabernet sauvignon', 'blaufrankisch')
            }

        },
        'white': {
            'light': {
                'portugal': ('loureiro', 'alvarinho'),
                'france': ('chardonnay', 'muscadet', 'chenin blanc'),
                'spain': ('alvarinho',),
                'italy': ('trebbiano',),
                'others': ('riesling', 'sylvaner')
            },
            'medium': {
                'france': ('chenin blanc', 'riesling', 'chardonnay', 'pinot gris'),
                'spain': ('torrontés', 'alvarinho'),
                'italy': ('verdicchio',)
            },
            'full': {
                'france': ('chardonnay',)
            }
        }
    }


def clause_country(mydict):
    country = mydict['country']

    if country != 'others':
        res = f"(country = '{country}')"

        return res

    country = countries[mydict['wtype']]
    res = f"country NOT IN {country}".replace(',)', ')')

    return res


def clause_grape(mydict):
    if 'grape' not in mydict:
        return ''

    grape = mydict['grape']

    if grape != 'other':
        res = f"(grape LIKE '%{grape}%')"

        return res

    grape = grapes[mydict['wtype']][mydict['wstyle']][mydict['country']]
    res = f"grape NOT IN {grape}".replace(',)', ')')

    return res


def execute_query(query):
    # Connect to db
    connection = psycopg2.connect(db_uri, sslmode='require')
    cursor = connection.cursor()

    try:
        # Execute the query
        cursor.execute(query)

        # Commit the transaction
        connection.commit()

        # Fetch the results
        result = cursor.fetchall()
        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


# get wine_id based on the user's criteria
def get_filtered(my_dict):
    # Make a copy of dict to save the original dict
    user_dict = my_dict.copy()

    # Create price min/max keys and clause
    user_dict['min_price'], user_dict['max_price'] = map(int, user_dict.pop('price', None).split('_'))
    where_filters = [f"(price >= {user_dict.pop('min_price', None)} AND price < {user_dict.pop('max_price', None)})",
                     f"(stock = True)"]

    # Create clause country
    fltr = clause_country(user_dict)
    where_filters.append(fltr)

    # Create clause grape
    fltr = clause_grape(user_dict)
    where_filters.append(fltr)

    # Delete unneeded keys
    for k in ('lang', 'step', 'country', 'grape'):
        user_dict.pop(k, None)

    # Create the rest of clauses
    for k, v in user_dict.items():
        clause = f"({k} = '{v}')"
        where_filters.append(clause)

    # Construct the SELECT query
    where_clause = ' AND '.join(where_filters)
    print(where_clause)
    select_query = sql.SQL(f"SELECT wine_id FROM specifications WHERE {where_clause}")

    # Execute the query
    values = execute_query(select_query)
    result = [value[0] for value in values]
    print('wineids', result)

    return result


# get descriptions based on the wine_ids
def get_description(list_of_ids, user_id, lang=0, complete=True):
    # choose the table
    table_name = f"description_{['rus', 'eng'][lang]}"

    # choose the list of attributes
    lst_attr = ['wine_id', 'title', 'price']
    if complete:
        lst_attr = ['wine_id', 'wtype', 'country', 'region', 'title', 'collection', 'volume', 'price',
                    'wstyle', 'sugar', 'grape', 'alcohol', 'bouquet', 'palate', 'food']

    # create where clause based on wine_ids
    where_ids = ', '.join(map(str, list_of_ids))

    # create attributes for SELECT
    query_attr = ', '.join(lst_attr)

    # Construct the SELECT query
    select_query = sql.SQL(f"SELECT {query_attr} FROM {table_name} WHERE wine_id IN ({where_ids})")

    # Execute the query
    values = execute_query(select_query)

    res_dict_list = [dict(zip(lst_attr, tpl)) for tpl in values]
    results = {user_id: res_dict_list}

    return results


def get_photo(wine_id):
    file_url = os.getenv('file_img_url')
    photo_url = file_url + f"{wine_id}.png"

    if requests.head(photo_url).status_code != 200:
        photo_url = file_url + 'noname.png'

    return photo_url