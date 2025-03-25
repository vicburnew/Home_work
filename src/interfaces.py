import re
import collections
from collections import Counter

from src.widget import get_date, mask_account_card
from tests.conftest import filter_by_description_list_final


def user_welcome_input() -> int:
    """Функция приветствия в начале программы и обработки выбора источника
    данных - JSON, CSV или XLSX файл"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    while True:
        try:
            user_input_1 = int(input(
                "Выберите необходимый пункт меню:\n "
                "1. Получить информацию о транзакциях из JSON-файла\n "
                "2. Получить информацию о транзакциях из CSV-файла\n "
                "3. Получить информацию о транзакциях из XLSX-файла\n"))

            if user_input_1 == 1:
                print('Для обработки выбран JSON-файл.\n')
                break
            elif user_input_1 == 2:
                print('Для обработки выбран CSV-файл.\n')
                break
            elif user_input_1 == 3:
                print('Для обработки выбран XLSX-файл.\n')
                break
            else:
                print("Введен неправильный номер, повторите ввод! \n\n")
        except Exception as ex:
            print(f"Ошибка ввода {ex}, повторите ввод!\n\n")
    return user_input_1


def user_status_input() -> str:
    """Функция, с помощью которой пользователь выбирает статус интересующих его
    операций - EXECUTED, CANCELED, PENDING"""
    while True:
        user_input_2 = input(
            "Введите статус, по которому необходимо выполнить фильтрацию\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").lower()

        if user_input_2 == "executed":
            print('Операции отфильтрованы по статусу "EXECUTED".\n')
            break
        elif user_input_2 == "canceled":
            print('Операции отфильтрованы по статусу "CANCELED".\n')
            break
        elif user_input_2 == 'pending':
            print('Операции отфильтрованы по статусу "PENDING".\n')
            break
        else:
            print(f"Статус операции {user_input_2} недоступен. \n\n")
    return user_input_2


def user_input_fbd() -> bool:
    """Функция, с помощью которой программа выводит уточняющий
     вопрос для выборки операций, необходимых пользователю,
     'fbd' =  filter by date"""
    filter_by_date_status = False
    user_input_3 = input(
        "Отсортировать операции по дате? Да/Нет \n").lower()
    if user_input_3 == "да":
        filter_by_date_status = True
    else:
        print(f"Вы ввели {user_input_3}, это значит 'Нет'. \n\n")
    return filter_by_date_status


def user_input_sbda() -> bool:
    """Функция, с помощью которой программа выводит уточняющий
         вопрос для выборки операций, необходимых пользователю
         'sbda' = sort by date ascending"""
    sort_date_by_ascending = True
    user_input_4 = input(
        "Отсортировать даты по возрастанию или по убыванию? \n").lower()
    if user_input_4 == "по возрастанию":
        sort_date_by_ascending = False
    else:
        print(f"Вы ввели {user_input_4}, это значит 'По убыванию'. \n\n")
    return sort_date_by_ascending


def user_input_rf() -> bool:
    """Функция, с помощью которой программа выводит уточняющий
         вопрос для выборки операций, необходимых пользователю
         'rf' = ruble filter"""
    show_only_rub_transactions = False
    user_input_5 = input(
        "Выводить только рублевые транзакции? Да/Нет \n").lower()
    if user_input_5 == "да":
        show_only_rub_transactions = True
    else:
        print(f"Вы ввели {user_input_5}, это значит 'Нет'. \n\n")
    return show_only_rub_transactions


def user_input_sw() -> bool:
    """Функция, с помощью которой программа выводит уточняющий
         вопрос для выборки операций, необходимых пользователю
         'sw' = specific word"""
    filter_by_specific_word = False
    user_input_6 = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n").lower()
    if user_input_6 == "да":
        filter_by_specific_word = True
    else:
        print(f"Вы ввели {user_input_6}, это значит 'Нет'. \n\n")
    return filter_by_specific_word


def filter_by_description(list_of_dicts: list[dict], look_up_str: str) -> list[dict]:
    """Функция принимает на вход список словарей с данными о банковских
    операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    filtered_list = []
    if look_up_str == "" or look_up_str == " ":
        filtered_list = list_of_dicts
        return filtered_list

    for dict_ in list_of_dicts:
        text = dict_.get("description")
        look_up_result = re.findall(look_up_str, text, re.IGNORECASE)
        if len(look_up_result) != 0:
            filtered_list.append(dict_)
    if len(filtered_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        filtered_list = list_of_dicts

    return filtered_list


def count_operations_by_type(list_of_dicts: list[dict], list_of_types_: list) -> dict:
    """Функция принимает на вход список словарей с данными о
    банковских операциях и список категорий операций, и возвращает словарь,
    в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории"""
    types_list_united = []
    for dict_ in list_of_dicts:
        if dict_["description"] in list_of_types_:
            types_list_united.append(dict_["description"])
    counted_types = dict(Counter(types_list_united))

    return counted_types


a = [{'amount': '23182',
             'currency_code': 'RUB',
             'currency_name': 'Ruble',
             'date': '2021-07-08T07:31:21Z',
             'description': 'Перевод с карты на карту',
             'from': 'Visa 0773092093872450',
             'id': '4234093',
             'state': 'EXECUTED',
             'to': 'Discover 8602781449570491'},
            {'amount': '18420',
             'currency_code': 'RUB',
             'currency_name': 'Ruble',
             'date': '2023-08-30T00:58:36Z',
             'description': 'Перевод с карты на карту',
             'from': 'Mastercard 3093124722348405',
             'id': '1473389',
             'state': 'EXECUTED',
             'to': 'American Express 6950002720800411'},
            {'amount': '21574',
             'currency_code': 'RUB',
             'currency_name': 'Ruble',
             'date': '2021-12-03T14:07:06Z',
             'description': 'Перевод со счета на счет',
             'from': 'Счет 22246813624466689601',
             'id': '212502',
             'state': 'EXECUTED',
             'to': 'Счет 60148056083328746527'},
            {'amount': '31741',
             'currency_code': 'RUB',
             'currency_name': 'Ruble',
             'date': '2023-10-20T21:00:39Z',
             'description': 'Перевод с карты на карту',
             'from': 'American Express 5313948287096164',
             'id': '3436241',
             'state': 'EXECUTED',
             'to': 'Discover 0329774489991288'},
            {'amount': '22818',
             'currency_code': 'RUB',
             'currency_name': 'Ruble',
             'date': '2022-03-25T01:54:48Z',
             'description': 'Перевод организации',
             'from': 'American Express 5289343085624249',
             'id': '3036684',
             'state': 'EXECUTED',
             'to': 'Счет 37876144219366357273'}]

b = [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        },
        {
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "id": 41428829,
            "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 35383033474447895560",
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "id": 587085106,
            "operationAmount": {"amount": "48223.05", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 41421565395219882431",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        }]



def program_output_1(list_of_dicts: list[dict]) -> None:
    """Функция вывода результатов работы программы в консоль (JSON)"""
    for dict_ in list_of_dicts:
        date = get_date(dict_["date"])
        descrp = dict_["description"]
        from_ = mask_account_card(dict_.get("from", "0"))
        to_ = mask_account_card(dict_["to"])
        summa = float(dict_["operationAmount"]["amount"])
        currency_name = dict_["operationAmount"]["currency"]["name"]
        print(f"{date} {descrp}\n {from_} -> {to_}\n Сумма: {summa} {currency_name}\n")

    return


def program_output_2(list_of_dicts: list[dict]) -> None:
    """Функция вывода результатов работы программы в консоль (CSV, EXCEL)"""
    for dict_ in list_of_dicts:
        date = get_date(dict_["date"])
        descrp = dict_["description"]
        from_ = mask_account_card(dict_["from"])
        to_ = mask_account_card(dict_["to"])
        summa = float(dict_.get("amount"))
        currency_name_2 = dict_.get("currency_code")
        print(f"{date} {descrp}\n {from_} -> {to_}\n Сумма: {summa} {currency_name_2}\n")

    return

program_output_1(b)

# program_output_2(a)
