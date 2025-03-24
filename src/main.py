from src.generators import filter_by_currency
from src.interfaces import user_welcome_input, user_status_input, user_input_fbd, user_input_sbda, user_input_rf, \
    user_input_sw
from src.processing import filter_by_state, sort_by_date, filter_by_currency_2, filter_by_currency_3
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
    # Вызываем функцию фильтрации, возвращающей отфильтрованный по статусу список словарей
    filtered_list = filter_by_state(list_of_dicts, status_selection)
    # Запрашиваем у пользователя, требуется ли сортировка по дате:
    user_fbd = user_input_fbd()
    if user_fbd:
    # Если да, то уточняем порядок сортировки - по возрастанию или по убыванию:
        user_sbda = user_input_sbda()
        if user_sbda is not True:
            filtered_list = sort_by_date(filtered_list, user_sbda)
    # Далее уточняем, выводить ли только рублевые трансакции:
    user_rf = user_input_rf()
    if user_rf:
        if user_selection != 1:
            filtered_list = filter_by_currency_2(filtered_list, "RUB")
        else:
            filtered_list = filter_by_currency_3(filtered_list, "RUB")

    print(filtered_list)

    user_sw = user_input_sw()



    # list_of_dicts = read_json_file("../data/")
    # print(filter_by_description(list_of_dicts, "Перевод"))

    return None

if __name__ == '__main__':
    main()
