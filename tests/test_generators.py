from src.generators import filter_by_currency


def test_filter_by_currency(transactions, transactions_USD_1):
    a = filter_by_currency(transactions, "USD")
    assert list(next(a)) == transactions_USD_1

