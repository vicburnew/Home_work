from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file, filter_by_description
from src.widget import get_date, mask_account_card

def main() -> None:
    list_of_dicts = read_json_file("./data/")
    print(filter_by_description(list_of_dicts, "Перевод"))

    return None

if __name__ == '__main__':
    main()
