def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_number_str = str(card_number)
    group_1 = card_number_str[:4] + " "
    group_2 = card_number_str[4:8]
    group_3 = "**** "
    group_4 = card_number_str[12:]
    group_2_new = group_2[:2] + "** "
    card_number_mask = group_1 + group_2_new + group_3 + group_4
    return card_number_mask


def get_mask_account(user_account: int) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""
    account_str = str(user_account)
    account_mask = "**" + account_str[-4:]
    return account_mask
