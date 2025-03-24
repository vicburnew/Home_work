from src.interfaces import user_welcome_input, user_status_input, user_input_fbd, user_input_sbda, user_input_rf, \
    user_input_sw
from src.processing import filter_by_state
from src.reading_csv_excel import read_csv_file, read_excel_file
from src.utils import read_json_file


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и
    связывает функциональности между собой."""
    list_of_dicts = []
    # Запрашиваем ввод источника данных (1,2 или 3):
    user_selection = user_welcome_input()
    if user_selection == 1:
        # Вызываем функцию чтения JSON - файла, возвращающей список словарей
        list_of_dicts = read_json_file("../data/")
    elif user_selection == 2:
        # Вызываем функцию чтения CSV - файла, возвращающей список словарей
        list_of_dicts = read_csv_file("../data/")
    else:
        # Вызываем функцию чтения EXCEL - файла, возвращающей список словарей
        list_of_dicts = read_excel_file("../data/")
    # Запрашиваем ввод статуса для фильтрации (executed, canceled, pending)
    # c переводом в верхний регистр:
    status_selection = user_status_input().upper().strip()
    # Вызываем функцию фильтрации, возвращающей отфильтрованный список словарей
    filtered_list = filter_by_state(list_of_dicts, status_selection)
    print(filtered_list)

    user_fbd = user_input_fbd()
    user_sbda = user_input_sbda()
    user_rf = user_input_rf()
    user_sw = user_input_sw()



    # list_of_dicts = read_json_file("../data/")
    # print(filter_by_description(list_of_dicts, "Перевод"))

    return None

if __name__ == '__main__':
    main()
