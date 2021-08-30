from random import random, randint, choice
from string import whitespace
import requests
import re

symbols = {
    'ƒ': ['Aruba Guilder','AWG'],
    '₼': ['Azerbaijan Manat','AZN'],
    '៛': ['Cambodia Riel','KHR'],
    '₡': ['Costa Rica Colon','CRC'],
    '₱': ['Cuba Peso','CUP'],
    '€': ['Euro Member Countries','EUR'],
    '¢': ['Ghana Cedi','GHS'],
    '₪': ['Israel Shekel','ILS'],
    '¥': ['Japan Yen','JPY'],
    '₩': ['Korea (South) Won','KRW'],
    '₭': ['Laos Kip','LAK'],
    '₮': ['Mongolia Tughrik','MNT'],
    '₦': ['Nigeria Naira','NGN'],
    '₽': ['Russia Ruble','RUB'],
    '฿': ['Thailand Baht','THB'],
    '₴': ['Ukraine Hryvnia','UAH'],
    '£': ['United Kingdom Pound','GBP'],
    '$': ['United States Dollar','USD'],
    '₫': ['Viet Nam Dong','VND']
}

def fill_wallet(operations):
    output = []
    for _ in range(operations):
        if random() < 0.25:
            output.append(get_currency())
        else:
            output.append(choice(whitespace))
    return output

def get_currency():
    return f'{choice(list(symbols.keys()))}{get_nums()}{get_cents()}'

def get_nums():
    return str(randint(0, 5000))

def get_cents():
    if random() < 0.5:
        return ''
    return '.' + str(randint(0, 99)).zfill(2)

with open('wallet.txt', 'w', encoding='utf-16') as f:
    f.writelines(fill_wallet(1000))


"""YOUR CODE TO CONVERT THE CURRENCIES INSIDE THE WALLET GOES BELOW"""
def read_wallet():
    with open('wallet.txt', 'r' , encoding='utf-16') as file:
        wallet = file.read()
    return wallet

def get_rates_from_api():
    request = requests.get("https://open.er-api.com/v6/latest/USD").json()
    return request['rates']

def get_conversion_rate(symbol, amount, rates):
    symbol_info = symbols.get(symbol)[1]
    converted_amount = amount / rates.get(symbol_info)
    return converted_amount

def clean_wallet():
    white_list = list(whitespace)
    wallet = read_wallet()
    for white_item in white_list:
        wallet = wallet.replace(white_item, '')
    return wallet
    
def create_tuple_of_symbol_amount(list_of_symbols):
    symbols_as_string = "".join(list_of_symbols)
    return re.findall(f"([{symbols_as_string}])*([\d,.]*)", wallet)


if __name__ == "__main__":
    wallet_sum = 0
    rates = get_rates_from_api()
    wallet = clean_wallet()
    list_of_symbols = list(symbols.keys())
    tuples_symbol_amount = create_tuple_of_symbol_amount(list_of_symbols)
    for tuple_of_symbol_amount in tuples_symbol_amount:
        symbol, amount = tuple_of_symbol_amount
        if symbol in list_of_symbols:
            wallet_sum += get_conversion_rate(symbol, float(amount), rates)
    print(f"${round(wallet_sum,2):,}")
