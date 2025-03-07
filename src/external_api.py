import os

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

    if currency_code == "RUB":
        rub_amount = round(float(currency_amount), 2)
        return rub_amount

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": currency_amount, "from": currency_code, "to": "RUB"}
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        raise Exception ("проверьте параметры запроса и повторите его")

    result = response.json()

    rub_amount = round(float(result["result"]),2)

    return rub_amount

