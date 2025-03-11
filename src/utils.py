import json
import logging

# Создание объекта логера для записи событий
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("./logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        logger.info("Начало, чтение файла 'operations.json'")
        full_path = path_to_file + "operations.json"
        try:
            with open(full_path, "r", encoding="utf-8") as json_file:
                list_result = json.load(json_file)
            logger.info("Чтение файла 'operations.json' успешно")
        except json.JSONDecodeError as ex:
            logger.error(f"Ошибка чтения файла 'operations.json', ошибка: {ex}")
            print("Ошибка декодирования файла или пустой файл")
            list_result = []
    except FileNotFoundError as ex:
        logger.error(f"Ошибка чтения файла 'operations.json' - неправильное имя или путь к файлу, ошибка: {ex}")
        print("Файл не найден")
        list_result = []

    return list_result
