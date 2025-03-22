
def filter_by_description(list_of_dicts: list[dict], look_up_str: str ) -> list[dict]:
    """Функция принимает на вход список словарей с данными о банковских
    операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    filtered_list = []
    for dict_ in list_of_dicts:
        text = dict_.get("description")
        # print(text)
        look_up_result = re.search(look_up_str, text, re.IGNORECASE)
        # print(look_up_result)
        if look_up_result.group():
            filtered_list.append(dict_)
        else:
            print("По запрошенному слову операции отсутствуют")

    return filtered_list

