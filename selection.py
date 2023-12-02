import requests
from io import StringIO
import pandas as pd
from dotenv import load_dotenv
import os

mdict = {}

load_dotenv()
token_ws = os.getenv('TOKEN_WS')
file_path = os.getenv('file_wine_to_select_url')

headers = {'Authorization': f'token {token_ws}'}
response = requests.get(file_path, headers=headers)
df_ws = pd.read_csv(StringIO(response.text))

def get_filtered(user_dict):
        filters = []
        print('user_dict ', user_dict)

        min_price, max_price = map(int, user_dict['wine_price'].split('_'))
        price_filter = (df_ws['price'] >= min_price) & (df_ws['price'] <= max_price)
        filters.append(price_filter)

        for key, value in user_dict.items():
                if key in df_ws.columns:
                        filters.append(df_ws[key] == value)

        final_filter = pd.Series(True, index=df_ws.index)
        for filt in filters:
                final_filter &= filt
        df_filtered = df_ws[final_filter]
        res = list(df_filtered['wine_id'])

        return res