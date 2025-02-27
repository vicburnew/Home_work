from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest

from tests.conftest import transactions, cards_1


# Тестирование функции test_filter_by_currency

def test_filter_by_currency(transactions, transactions_USD_1):
    """Положительный тест на проверку фильтрации по USD"""
    a = filter_by_currency(transactions, "USD")
    assert list(next(a)) == transactions_USD_1

def test_filter_by_currency_2(transactions, transactions_RUB):
    """Положительный тест на проверку фильтрации по рублям"""
    a = filter_by_currency(transactions, "RUB")
    assert list(next(a)) == transactions_RUB

@pytest.mark.parametrize("empty_list", [{}])
def test_filter_by_currency_3(empty_list):
    """Отрицательный тест - пустой список на входе"""
    with pytest.raises(TypeError):
        a = filter_by_currency(empty_list, "EUR")
        list(next(a))

def test_filter_by_currency_4(transactions_no_curr):
    """Отрицательный тест на проверку отсутствие транзакций в заданной валюте
    или списка без соответствующих валютных операций"""
    a = filter_by_currency(transactions_no_curr, "USD")
    with pytest.raises(TypeError):
        a = filter_by_currency(transactions_no_curr, "USD")
        list(next(a))

# Тестирование функции transaction_descriptions

def test_transaction_descriptions(transactions, descriptions):
    """Положительный тест на возврат корректных описаний для каждой транзакции"""
    a = transaction_descriptions(transactions)
    assert list(next(a)) == descriptions

def test_transaction_descriptions_2():
    """Отрицательный тест на пустой список"""
    a = transaction_descriptions([])
    with pytest.raises(TypeError):
        list(next(a))

# Тестирование функции card_number_generator

# @pytest.mark.parametrize("start, stop", "result",
#                          [(1, 2, "0000 0000 0000 0001")])
def test_card_number_generator():
    for card_number_2 in card_number_generator(1, 5):
        assert card_number_2 == [
                                            "0000 0000 0000 0001",
                                            "0000 0000 0000 0002",
                                            "0000 0000 0000 0003",
                                            "0000 0000 0000 0004",
                                            "0000 0000 0000 0005"]


