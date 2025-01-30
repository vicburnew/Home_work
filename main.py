from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

# print(get_mask_card_number(7000792289606361))
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


# print(get_mask_account(73654108430135874305))
# 73654108430135874305  # входной аргумент
# **4305  # выход функции

print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
# Счет 73654108430135874305  # входной аргумент
# Счет **4305  # выход функции