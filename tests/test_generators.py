from src.generators import filter_by_currency


def test_filter_by_currency(transactions, transactions_USD_1):
    """Положительный тест на проверку фильтрации по USD"""
    a = filter_by_currency(transactions, "USD")
    assert list(next(a)) == transactions_USD_1

def test_filter_by_currency_2(transactions, transactions_RUB):
    """Положительный тест на проверку фильтрации по рублям"""
    a = filter_by_currency(transactions, "RUB")
    assert list(next(a)) == transactions_RUB
