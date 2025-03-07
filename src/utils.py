import json


def read_json_file(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        full_path = path_to_file + "operations.json"
        try:
            with open(full_path, "r", encoding="utf-8") as json_file:
                list_result = json.load(json_file)
        except json.JSONDecodeError:
            print("Ошибка декодирования файла или пустой файл")
            list_result = []
    except FileNotFoundError:
        print("Файл не найден")
        list_result = []

    return list_result
