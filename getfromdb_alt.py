import os
import requests
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import random

import my_dict

load_dotenv()
db_uri = os.getenv('DB_URI')

countries = {k: v[-1][:-1] for k, v in my_dict.dict_categories['country'].items()}
grapes = {
        'red': {
            'light': {
                'france': ('gamay', 'pinot noir'),
                'spain': ('garnacha', 'mencia'),
                'italy': ('barbera', 'corvina', 'dolcetto', 'sangiovese')
            },
            'medium': {
                'france': ('cabernet franc', 'carignan', 'côt', 'grenache', 'merlot', 'syrah'),
                'spain': ('carignan', 'mencia', 'tempranillo'),
                'italy': ('montepulciano', 'nebbiolo', 'primitivo', 'sangiovese')
            },
            'full': {
                'france': ('cabernet sauvignon', 'merlot', 'mourvèdre', 'syrah'),
                'spain': ('monastrell', 'tempranillo'),
                'italy': ('aglianico', 'nebbiolo', 'primitivo', 'sangiovese'),
                'others': ('cabernet sauvignon', 'blaufrankisch', 'malbec')
            }
        },
        'white': {
            'light': {
                'portugal': ('alvarinho', 'loureiro'),
                'france': ('chardonnay', 'sauvignon blanc', 'grenache blanc', 'muscadet'),
                'spain': ('albariño', 'verdejo'),
                'italy': ('glera', 'moscato', 'pinot grigio', 'trebbiano'),
                'others': ('riesling', 'sylvaner')
            },
            'medium': {
                'france': ('chardonnay', 'chenin blanc', 'riesling', 'viognier'),
                'spain': ('airén', 'albariño', 'torrontés', 'viura'),
                'italy': ('chardonnay', 'pinot bianco', 'verdicchio', 'vermentino')
            },
            'full': {
                'france': ('chardonnay', 'gewurztraminer', 'riesling', 'viognier'),
                'spain': ('albariño', 'garnacha blanca'),
                'italy': ('fiano di avellino', 'verdicchio')
            }
        }
    }

regions = {
        'red': {
                'portugal': ('alentejo', 'bairrada', 'dão', 'douro', 'lisboa', 'vinho verde'),
                'france': ('bordeaux', 'bourgogne', 'loire', 'rhône', 'other'),
                'spain': ('ribera del duero', 'rioja'),
                'italy': ('piemonte', 'puglia', 'toscana', 'veneto')
        },
        'white': {
                'portugal': ('alentejo', 'bairrada', 'dão', 'douro', 'lisboa', 'vinho verde'),
                'france': ('alsace', 'bordeaux', 'bourgogne', 'loire'),
                'spain': ('canarias', 'galicia'),
                'italy': ('abruzzo', 'alto adige', 'sicilia', 'toscana')
        }
    }
incr_idx = -1


def clause_country(mydict):
    country = mydict['country']

    if country != 'others':
        res = f"(country = '{country}')"

        return res

    country = countries[mydict['wtype']]
    res = f"country NOT IN {country}".replace(',)', ')')

    return res


def clause_region(mydict):
    region = mydict['region']

    if region != 'other':
        res = f"(region = '{region}')"

        return res

    region = regions[mydict['wtype']][mydict['country']]
    res = f"region NOT IN {region}".replace(',)', ')')

    return res


def clause_grape(mydict):
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


# check region, grapes, country in keys and remove them
def remove_keys(dict_to_change):
    dict_to_change = dict_to_change.copy()

    if 'region' in dict_to_change or 'grape' in dict_to_change:
        dict_to_change.pop('region', None)
        dict_to_change.pop('grape', None)

        return dict_to_change

    elif 'country' in dict_to_change:
        dict_to_change.pop('country', None)

        return dict_to_change

    dict_to_change['price'] = change_price(dict_to_change['price'])

    return dict_to_change


def change_price(price):
    global incr_idx

    price_idx = my_dict.dict_categories['price'][2].index(price)
    if price_idx == 0:
        incr_idx = 1

    price_idx += incr_idx
    print('price', my_dict.dict_categories['price'][2][price_idx])

    return my_dict.dict_categories['price'][2][price_idx]


# get wine_id based on the user's criteria
def get_filtered(mydict):
    # Set flag points original request from user or modified
    ff = True

    # Make a copy of dict to save the original dict
    user_dict = mydict.copy()

    # Create price min/max keys and clause
    user_dict['min_price'], user_dict['max_price'] = map(int, user_dict.pop('price', None).split('_'))
    where_filters = [f"(price >= {user_dict.pop('min_price', None)} AND price < {user_dict.pop('max_price', None)})",
                     f"(stock = True)"]

    # Delete unneeded keys
    for k in ('lang', 'step', 'wine_cart'):
        user_dict.pop(k, None)

    # Create the rest of clauses
    for k, v in user_dict.items():
        if k == 'grape':
            clause = clause_grape(user_dict)
        elif k == 'country':
            clause = clause_country(user_dict)
        elif k == 'region':
            clause = clause_region(user_dict)
        else:
            clause = f"({k} = '{v}')"
        where_filters.append(clause)

    # Construct the SELECT query
    where_clause = ' AND '.join(where_filters)
    print(where_clause)
    select_query = sql.SQL(f"SELECT wine_id FROM specifications WHERE {where_clause}")

    # Execute the query
    values = execute_query(select_query)

    result = [value[0] for value in values]
    if not result:
        changed_dict = remove_keys(mydict)
        result, ff = get_filtered(changed_dict)
        ff = False

    print('wineids', result)
    # set the number of wines to show in case our suggestion
    number_to_show = 4
    if not ff:
        result = random.sample(result, number_to_show) if len(result) >= number_to_show else result

    return result, ff


# get descriptions based on the wine_ids
def get_description(list_of_ids, user_id, lang=0, complete=True):
    # choose the table
    table_name = f"description_{['rus', 'eng'][lang]}"

    # choose the list of attributes
    lst_attr = ['wine_id', 'title', 'region', 'collection', 'price', 'wtype', 'wstyle', 'sugar']
    if complete:
        lst_attr = ['wine_id', 'wtype', 'country', 'region', 'subregion', 'title',
                    'maker', 'collection', 'volume', 'price', 'wstyle', 'sugar',
                    'grape', 'alcohol', 'bouquet', 'palate', 'food']

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
    photo_url = file_url + f"aw_n{wine_id}.png"

    if requests.head(photo_url).status_code != 200:
        photo_url = file_url + 'grapes.jpg'

    return photo_url


# check if delivery address already exist and return it
def check_exist_address(user_id):

    select_query = sql.SQL(f"SELECT zip_code, address, phone, customer_name "
                           f"FROM specifications WHERE user_id = {user_id}")

    # execute the query
    values = execute_query(select_query)
    print(values)
