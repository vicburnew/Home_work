def filter_by_state(list_of_dict: list[dict], state_by_default: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state  соответствует указанному значению."""

    new_list = []

    for dict_ in list_of_dict:
        if dict_.get("state") == state_by_default:
            new_list.append(dict_)
    return new_list


def sort_by_date(list_of_dict: list[dict], sort_type: bool = True) -> list[dict]:
    """Функция принимает на вход список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате."""

    list_of_dict_sorted = sorted(list_of_dict, key=lambda x: (x["date"], x["id"]), reverse=sort_type)
    return list_of_dict_sorted


def filter_by_currency_2(list_of_dict: list[dict], currency: str) -> list[dict]:
    """Функция принимает список словарей из файлов CSV и EXCEL и код валюты. Функция возвращает
    новый список словарей, содержащий только те словари,
    у которых ключ currency_code соответствует указанному значению."""
    result = [dict_ for dict_ in list_of_dict if dict_.get("currency_code") == currency]
    return result


def filter_by_currency_3(list_of_dict: list[dict], currency: str) -> list[dict]:
    """Функция принимает список словарей из файла JSON и код валюты. Функция возвращает
    новый список словарей, содержащий только те словари,
    у которых ключ currency_code соответствует указанному значению."""
    result = [dict_ for dict_ in list_of_dict if dict_["operationAmount"]["currency"]["code"] == currency]
    return result
