import requests


def currency_rates(*args):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    r = response.text
    for arg in args:
        arg = arg.upper()
        if r.find(arg) != -1:
            text_list = r.split("</Value>")
            for element in text_list:
                if element.find(arg) != -1:
                    print(float(element[-7:].replace(',', '.')))
        else:
            print('None')
