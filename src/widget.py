from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(input_long_data:str) -> str:
    """Функция, которая принимает один аргумент — строку, 
        содержащую тип и номер карты или счета, и возвращает строку
        с замаскированным номером"""
    long_input_masked = ""
    # переводим вход в нижний регистр
    input_long_data_low = input_long_data.lower()
    # превращаем строку в лист
    input_data_list = input_long_data_low.split()
    # вырезаем номер карты или счета
    num_code = int(input_data_list[-1])
    # проверяем, что у нас было на входе - карта или счет
    if input_data_list[0] != "счет":
        # если была карта, то вызываем функцию маскировки номера карты, на
        # выходе получаем маску номера карты
        mask_1 = get_mask_card_number(num_code)
        input_data_list[-1] = mask_1
        long_input_masked_low = " ".join(input_data_list)
        long_input_masked = long_input_masked_low.title()
    else:
        # если был счет, то вызываем функцию маскировки номера счета, на
        # выходе получаем маску номера счета
        mask_2 = get_mask_account(num_code)
        input_data_list[-1] = mask_2
        long_input_masked_low = " ".join(input_data_list)
        long_input_masked = long_input_masked_low.title()

    return long_input_masked

