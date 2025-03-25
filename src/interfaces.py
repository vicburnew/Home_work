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


a = [{'id': '4234093', 'state': 'EXECUTED', 'date': '2021-07-08T07:31:21Z', 'amount': '23182', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 0773092093872450', 'to': 'Discover 8602781449570491',
      'description': 'Перевод с карты на карту'},
     {'id': '1473389', 'state': 'EXECUTED', 'date': '2023-08-30T00:58:36Z', 'amount': '18420', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 3093124722348405', 'to': 'American Express 6950002720800411',
      'description': 'Перевод с карты на карту'},
     {'id': '212502', 'state': 'EXECUTED', 'date': '2021-12-03T14:07:06Z', 'amount': '21574', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 22246813624466689601', 'to': 'Счет 60148056083328746527',
      'description': 'Перевод со счета на счет'},
     {'id': '3436241', 'state': 'EXECUTED', 'date': '2023-10-20T21:00:39Z', 'amount': '31741', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'American Express 5313948287096164', 'to': 'Discover 0329774489991288',
      'description': 'Перевод с карты на карту'},
     {'id': '3036684', 'state': 'EXECUTED', 'date': '2022-03-25T01:54:48Z', 'amount': '22818', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'American Express 5289343085624249', 'to': 'Счет 37876144219366357273',
      'description': 'Перевод организации'},
     {'id': '2037712', 'state': 'EXECUTED', 'date': '2023-07-31T16:44:50Z', 'amount': '11562', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'American Express 6902837737884644', 'to': 'American Express 1368443024115273',
      'description': 'Перевод с карты на карту'},
     {'id': '4569563', 'state': 'EXECUTED', 'date': '2022-05-31T12:42:38Z', 'amount': '29532', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 9698316448168820', 'to': 'Счет 91507178049597221508',
      'description': 'Перевод организации'},
     {'id': '3691525', 'state': 'EXECUTED', 'date': '2021-03-14T07:31:40Z', 'amount': '12576', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Discover 8455447150087314', 'to': 'Счет 70453658863403233739',
      'description': 'Перевод организации'},
     {'id': '1608930', 'state': 'EXECUTED', 'date': '2022-04-24T07:33:16Z', 'amount': '18125', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 8817383202472795', 'to': 'Discover 3942175254816690',
      'description': 'Перевод с карты на карту'},
     {'id': '1938897', 'state': 'EXECUTED', 'date': '2022-09-09T01:21:13Z', 'amount': '20083', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 86244850477007883319', 'to': 'Счет 81698090448201122541',
      'description': 'Перевод со счета на счет'},
     {'id': '2407135', 'state': 'EXECUTED', 'date': '2022-08-07T12:37:13Z', 'amount': '15333', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Discover 6574691179829422', 'to': 'Discover 4659403386698758',
      'description': 'Перевод с карты на карту'},
     {'id': '4692041', 'state': 'EXECUTED', 'date': '2021-10-25T12:32:28Z', 'amount': '18106', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 7725500610751579', 'to': 'Discover 8189486607683162',
      'description': 'Перевод с карты на карту'},
     {'id': '5051972', 'state': 'EXECUTED', 'date': '2023-08-25T19:34:26Z', 'amount': '22833', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 57132829784776201423', 'to': 'Счет 95605694496875862934',
      'description': 'Перевод со счета на счет'},
     {'id': '2195935', 'state': 'EXECUTED', 'date': '2020-05-10T08:19:35Z', 'amount': '29722', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 7657178713716531', 'to': 'Mastercard 5442625865778510',
      'description': 'Перевод с карты на карту'},
     {'id': '4653425', 'state': 'EXECUTED', 'date': '2020-03-10T07:48:21Z', 'amount': '22131', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': '', 'to': 'Счет 58936710508356884628', 'description': 'Открытие вклада'},
     {'id': '1530853', 'state': 'EXECUTED', 'date': '2023-03-25T02:49:04Z', 'amount': '16225', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 3723527446109611', 'to': 'American Express 4201111974501655',
      'description': 'Перевод с карты на карту'},
     {'id': '3012438', 'state': 'EXECUTED', 'date': '2023-01-26T05:06:25Z', 'amount': '26980', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 36880956803774247605', 'to': 'Счет 57967135740972430525',
      'description': 'Перевод со счета на счет'},
     {'id': '2854238', 'state': 'EXECUTED', 'date': '2023-10-12T03:15:11Z', 'amount': '29511', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 4205969069978141', 'to': 'Mastercard 3182665825206884',
      'description': 'Перевод с карты на карту'},
     {'id': '4009886', 'state': 'EXECUTED', 'date': '2023-05-13T04:33:00Z', 'amount': '23989', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Discover 2343953148883158', 'to': 'American Express 8400869379923599',
      'description': 'Перевод с карты на карту'},
     {'id': '1991230', 'state': 'EXECUTED', 'date': '2022-12-20T01:52:57Z', 'amount': '21833', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 1399159034596740', 'to': 'Счет 71814990641193663905',
      'description': 'Перевод организации'},
     {'id': '2424241', 'state': 'EXECUTED', 'date': '2023-02-08T11:58:12Z', 'amount': '17867', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 1563074999448104', 'to': 'Visa 6133882980108564',
      'description': 'Перевод с карты на карту'},
     {'id': '5466732', 'state': 'EXECUTED', 'date': '2022-08-12T00:55:39Z', 'amount': '26278', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 0560253835243874', 'to': 'Счет 44603300489524463522',
      'description': 'Перевод организации'},
     {'id': '1083434', 'state': 'EXECUTED', 'date': '2023-08-28T08:03:34Z', 'amount': '27895', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 01411847038697732472', 'to': 'Счет 67457374082601064845',
      'description': 'Перевод со счета на счет'},
     {'id': '2455265', 'state': 'EXECUTED', 'date': '2021-09-06T03:06:29Z', 'amount': '33345', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 7986449445672194', 'to': 'Visa 8862361645542151',
      'description': 'Перевод с карты на карту'},
     {'id': '911993', 'state': 'EXECUTED', 'date': '2023-06-17T05:36:39Z', 'amount': '16143', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 8924432019137202', 'to': 'Visa 5653663363322651',
      'description': 'Перевод с карты на карту'},
     {'id': '1586405', 'state': 'EXECUTED', 'date': '2023-05-09T10:50:48Z', 'amount': '15292', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'American Express 0134021618597734', 'to': 'Mastercard 7974416741612242',
      'description': 'Перевод с карты на карту'},
     {'id': '555920', 'state': 'EXECUTED', 'date': '2021-06-26T04:51:42Z', 'amount': '12545', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Visa 3057946398768198', 'to': 'Discover 4035896941119221',
      'description': 'Перевод с карты на карту'},
     {'id': '1312600', 'state': 'EXECUTED', 'date': '2021-03-25T15:41:59Z', 'amount': '34455', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 00001929651993491151', 'to': 'Счет 94107008805088717279',
      'description': 'Перевод со счета на счет'},
     {'id': '811203', 'state': 'EXECUTED', 'date': '2021-09-15T11:34:48Z', 'amount': '32900', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Счет 36602273830151626580', 'to': 'Счет 61127622361324528517',
      'description': 'Перевод со счета на счет'},
     {'id': '4656334', 'state': 'EXECUTED', 'date': '2023-01-08T04:23:54Z', 'amount': '34114', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'American Express 9171903868456946', 'to': 'Visa 1486898442392527',
      'description': 'Перевод с карты на карту'},
     {'id': '651026', 'state': 'EXECUTED', 'date': '2021-07-10T20:52:54Z', 'amount': '27596', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': '', 'to': 'Счет 41878599375303475996', 'description': 'Открытие вклада'},
     {'id': '4967592', 'state': 'EXECUTED', 'date': '2021-11-21T16:57:36Z', 'amount': '12868', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 4061237171643434', 'to': 'Visa 7539829899017635',
      'description': 'Перевод с карты на карту'},
     {'id': '2300619', 'state': 'EXECUTED', 'date': '2020-06-12T18:50:27Z', 'amount': '32753', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Discover 8926691998863176', 'to': 'Discover 9331952063031046',
      'description': 'Перевод с карты на карту'},
     {'id': '3330422', 'state': 'EXECUTED', 'date': '2023-08-05T07:11:26Z', 'amount': '30065', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 9458117363112215', 'to': 'Visa 6335859532296628',
      'description': 'Перевод с карты на карту'}]


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
        # print(text)
        look_up_result = re.findall(look_up_str, text, re.IGNORECASE)
        print(look_up_result)
        if len(look_up_result) != 0:
            filtered_list.append(dict_)
    if len(filtered_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        filtered_list = list_of_dicts

    return filtered_list

# print(filter_by_description(a, "sasd"))
