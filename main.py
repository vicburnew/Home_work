from src.interfaces import (
    user_welcome_input,
    user_status_input,
    user_input_fbd,
    user_input_sbda,
    user_input_rf,
    user_input_sw,
    filter_by_description,
    count_operations_by_type,
    program_output_1,
    program_output_2,
)
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
        list_of_dicts = read_json_file("data/")
    elif user_selection == 2:
        # Вызываем функцию чтения CSV - файла, возвращающей список словарей
        list_of_dicts = read_csv_file("data/")
    else:
        # Вызываем функцию чтения EXCEL - файла, возвращающей список словарей
        list_of_dicts = read_excel_file("data/")
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
    # Далее запрашиваем, нужно ли фильтровать список по определенному слову.
    user_sw = user_input_sw()
    # Если "да", то пользователю предлагается ввести слово для фильтрации.
    # Если пользователь ввел слово, которого нет в поле "description", то программа
    # возвращает текущий список словарей с выводом предупреждения о том, что
    # -Не найдено ни одной транзакции, подходящей под ваши условия фильтрации-.
    if user_sw:
        specific_word = input("Введите слово для фильтрации: \n")
        filtered_list = filter_by_description(filtered_list, specific_word)
    print("Распечатываю итоговый список транзакций...\n")
    # Подготовка списка категорий (по умолчанию - все категории)
    list_of_types = ["Открытие вклада", "Перевод с карты на карту", "Перевод организации", "Перевод со счета на счет"]
    # Вызов функции подсчета количества банковских операций
    counted_list_of_types = count_operations_by_type(filtered_list, list_of_types)
    number_of_operations = sum(counted_list_of_types.values())
    # Вывод общего количества операций:
    print(f"Всего банковских операций в выборке: {number_of_operations}\n")
    # Вывод результатов работы программы в консоль:
    if user_selection != 1:
        program_output_2(filtered_list)
    else:
        program_output_1(filtered_list)

    return None


if __name__ == "__main__":
    main()
