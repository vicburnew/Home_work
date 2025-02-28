

def filter_by_currency(list_of_dict: list[dict], currency: str) -> any:
    """функция принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""

    if len(list_of_dict) == 0:
        raise (TypeError, "Некорректные входные данные")

    list_of_curr = ["USD", "RUB", "EUR"]
    for dict in list_of_dict:
        if dict["operationAmount"]["currency"]["code"] not in list_of_curr:
            raise (TypeError, "Неправильный тип валюты")

    result = filter(lambda x: (x["operationAmount"]["currency"]["code"] == currency), list_of_dict)
    return result


def transaction_descriptions(list_of_dict: list[dict]) -> str:
    """Генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""

    if len(list_of_dict) == 0:
        raise (TypeError, "Некорректные входные данные")

    result = (i["description"] for i in list_of_dict)
    yield result


def card_number_generator(start: int, end: int) -> str:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X  —
    цифра номера карты. Генератор может сгенерировать номера карт в заданном
    диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    null_number = "0000000000000000"

    if start <= 0 or end > 9999999999999999:
        raise (TypeError, "Неправильный номер")

    for card_num in range(start, end + 1):
        card_num_gen = null_number[: -len(str(card_num))] + str(card_num)
        result = card_num_gen[:4] + " " + card_num_gen[4:8] + " " + card_num_gen[8:12] + " " + card_num_gen[12:]

        yield result
