from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(7000792289606361))
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


print(get_mask_account(73654108430135874305))
# 73654108430135874305  # входной аргумент
# **4305  # выход функции
