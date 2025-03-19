
import pandas as pd
import csv


def read_csv_file(path_to_file: str) -> list[str]:
    """Функция принимает на вход путь к csv-файлу 'transactions.csv' и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    full_path = path_to_file + "transactions.csv"
    try:
        try:
            with open (full_path, encoding="utf-8") as file:
                csv_read_obj = csv.DictReader(file, delimiter=";")
                csv_list_result = [x for x in csv_read_obj]
        except Exception as ex:
            print(f"Ошибка чтения .csv файла, ошибка{ex}")
            csv_list_result = []
    except FileNotFoundError as ex:
        print(f"Неправильный путь к файлу или файл не найден, ошибка{ex}")
        csv_list_result = []
    return csv_list_result


def read_excel_file(path_to_file: str) -> list[str]:
    """Функция принимает на вход путь к excel-файлу 'transactions_excel.xlsx' и
    возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    full_path = path_to_file + "transactions_excel.xlsx"

    try:
        df_excel = pd.read_excel(full_path)
        excel_list_result = df_excel.to_dict(orient="records")
    except Exception as ex:
        print(f"Ошибка чтения .excel файла, ошибка: {ex}")
        excel_list_result = []
    return excel_list_result
