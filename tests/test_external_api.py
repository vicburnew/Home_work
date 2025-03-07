from src.external_api import convert_currency_to_rub


def test_convert_currency_to_rub_1(transactions_USD_1):
    """Положительный тест на работу функции по USD"""
    assert convert_currency_to_rub(transactions_USD_1) == 876795.27
