import requests
from io import StringIO, BytesIO
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()
token_ws = os.getenv('TOKEN_WS')
file_path = os.getenv('file_wine_url')

headers = {'Authorization': f'token {token_ws}'}
response = requests.get(file_path, headers=headers)
df = pd.read_csv(StringIO(response.text))

def getwine(list_of_ids, user_id, lang=0, complete=True):
    res_list = []

    result_df = df[df['wine_id'].isin(list_of_ids)]
    for i in result_df.index:
        if complete:
            description = 'description' + ['_rus', ''][lang]
            res_list.append({'wine_id': result_df.loc[i, 'wine_id'],
                             'title': result_df.loc[i, 'title'],
                             'description': result_df.loc[i, description]})
        else:
            res_list.append({'wine_id': result_df.loc[i, 'wine_id'],
                             'title': result_df.loc[i, 'title'],
                             'price': result_df.loc[i, 'price']})

    results = {user_id: res_list}

    return results


def getphoto(wine_id):
    file_url = os.getenv('file_img_url')
    photo_url = file_url + f"{wine_id}.png"

    if requests.head(photo_url).status_code != 200:
        photo_url = file_url + 'noname.png'

    #response = requests.get(photo_url)
    #photo = BytesIO(response.content)

    return photo_url