def wine_template(index, lngth, lang, wine):
    # Create list with headers and dictionary
    lst_header = ['wine', 'maker', 'rating', 'wtype', 'grape', 'region', 'price', 'bouquet', 'palate', 'food']
    dict_head = {}

    # Start description text from number of current position / amount of all position
    description_text = [f"{index + 1} "
                        f"{['из', 'of'][lang]} {lngth} "
                        f"{['найденных', 'found'][lang]}"]

    # Fill the dictionary for text output
    dict_head['wine'] = f"{['Вино:', 'Wine:'][lang]} <b>{wine.get('title', None)} " \
                        f"{wine.get('collection', '')}</b>".replace('None', '').rstrip()
    dict_head['maker'] = f"{['Пр-ль:', 'Producer:'][lang]} <i>{wine.get('maker', None)}</i>"
    dict_head['rating'] = f"{['Рейтинг:', 'Rating:'][lang]} {wine.get('rating', None)} ⭐"
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
