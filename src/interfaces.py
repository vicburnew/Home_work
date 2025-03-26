import re
from collections import Counter


from src.widget import get_date, mask_account_card


def user_welcome_input() -> int:
    """Функция приветствия в начале программы и обработки выбора источника
    данных - JSON, CSV или XLSX файл"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    while True:
        try:
            user_input_1 = int(
                input(
                    "Выберите необходимый пункт меню:\n "
                    "1. Получить информацию о транзакциях из JSON-файла\n "
                    "2. Получить информацию о транзакциях из CSV-файла\n "
                    "3. Получить информацию о транзакциях из XLSX-файла\n"
                )
            )

            if user_input_1 == 1:
                print("Для обработки выбран JSON-файл.\n")
                break
            elif user_input_1 == 2:
                print("Для обработки выбран CSV-файл.\n")
                break
            elif user_input_1 == 3:
                print("Для обработки выбран XLSX-файл.\n")
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
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).lower()

        if user_input_2 == "executed":
            print('Операции отфильтрованы по статусу "EXECUTED".\n')
            break
        elif user_input_2 == "canceled":
            print('Операции отфильтрованы по статусу "CANCELED".\n')
            break
        elif user_input_2 == "pending":
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
    user_input_3 = input("Отсортировать операции по дате? Да/Нет \n").lower()
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
    user_input_4 = input("Отсортировать даты по возрастанию или по убыванию? \n").lower()
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
    user_input_5 = input("Выводить только рублевые транзакции? Да/Нет \n").lower()
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
    user_input_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n").lower()
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
        # print(f">>>>>>>>>>>{look_up_result}")
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
        if len(str(dict_.get("from"))) > 3:
            from_ = mask_account_card(dict_.get("from", "0"))
        else:
            from_ = ""
        to_ = mask_account_card(dict_["to"])
        summa = float(dict_.get("amount"))
        currency_name_2 = dict_.get("currency_code")
        output_string = f"{date} {descrp}\n {from_} -> {to_}\n Сумма: {summa} {currency_name_2}\n"
        print(output_string)

    return
