from src.interfaces import user_welcome_input, user_status_input, user_input_fbd, user_input_sbda, user_input_rf, \
    user_input_sw


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и
    связывает функциональности между собой."""
    user_selection = user_welcome_input()
    status_selection = user_status_input()
    user_fbd = user_input_fbd()
    user_sbda = user_input_sbda()
    user_rf = user_input_rf()
    user_sw = user_input_sw()



    # list_of_dicts = read_json_file("../data/")
    # print(filter_by_description(list_of_dicts, "Перевод"))

    return None

if __name__ == '__main__':
    main()
