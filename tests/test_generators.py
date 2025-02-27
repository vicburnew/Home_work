from src.generators import filter_by_currency


def test_filter_by_currency(transactions, transactions_USD_1):
    assert filter_by_currency(transactions, "usd") == transactions_USD_1

