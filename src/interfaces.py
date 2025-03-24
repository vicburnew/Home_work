import re

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





def filter_by_description(list_of_dicts: list[dict], look_up_str: str ) -> list[dict]:
    """Функция принимает на вход список словарей с данными о банковских
    операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    filtered_list = []
    for dict_ in list_of_dicts:
        text = dict_.get("description")
        look_up_result = re.search(look_up_str, text, re.IGNORECASE)
        if look_up_result.group():
            filtered_list.append(dict_)
        else:
            print("По запрошенному слову операции отсутствуют")

    return filtered_list


