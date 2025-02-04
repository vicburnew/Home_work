def filter_by_state(list_of_dict: list[dict], state_by_default: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state  соответствует указанному значению."""

    new_list = []
    for dict_ in list_of_dict:
        if dict_.get("state") == state_by_default:
            new_list.append(dict_)
    return new_list


# list_A = [
# {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
# print(filter_by_state(list_A, "CANCELED"))
# print(filter_by_state(list_A))

# Примеры работы функции:
# Выход функции со статусом по умолчанию 'EXECUTED'
# [
# {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

# Выход функции, если вторым аргументов передано 'CANCELED'
# [
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]

# Пример входных данных для проверки функции
# [
# {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]
