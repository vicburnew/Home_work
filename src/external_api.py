import os
from pprint import pprint

from dotenv import load_dotenv
import requests

def convert_currency_to_rub(transaction:dict)->float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции
     (amount) в рублях, тип данных — float. Если транзакция была в USD или EUR,
     происходит обращение к внешнему API для получения текущего курса валют
     и конвертации суммы операции в рубли.
     Для конвертации валюты используется Exchange Rates Data API:
     https://apilayer.com/exchangerates_data-api. """
    currency_code = transaction["operationAmount"]["currency"]["code"]
    currency_amount = transaction["operationAmount"]["amount"]

    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": currency_amount, "from": currency_code, "to": "RUB"}
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return False
    result = response.json()

    rur_amount = round(float(result["result"]),2)

    return rur_amount
#
# pprint(convert_currency_to_rub({
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     }))