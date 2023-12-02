import os
import requests
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv


load_dotenv()
db_uri = os.getenv('DB_URI')


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

    # Delete unwanted keys
    del user_dict['lang']
    del user_dict['step']

    # Create price min/max keys and clause
    user_dict['min_price'], user_dict['max_price'] = map(int, user_dict.pop('price', None).split('_'))
    where_filters = [f"(price >= {user_dict.pop('min_price', None)} AND price < {user_dict.pop('max_price', None)})",
                     f"(stock = True)"]

    # Create the rest of clauses
    for k, v in user_dict.items():
        clause = f"({k} = '{v}')"
        if (k in ('country', 'grape')) and (not isinstance(v, str)):
            clause = f"{k} NOT IN {v}".replace(',)', ')')
        elif k == 'grape':
            clause = f"({k} LIKE '%{v}%')"
        where_filters.append(clause)

    # Construct the SELECT query
    where_clause = ' AND '.join(where_filters)
    select_query = sql.SQL(f"SELECT wine_id FROM specifications WHERE {where_clause}")

    # Execute the query
    values = execute_query(select_query)
    result = [value[0] for value in values]

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