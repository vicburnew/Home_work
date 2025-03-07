from unittest.mock import patch

import pytest

from src.external_api import convert_currency_to_rub


@patch("requests.get")
def test_convert_currency_to_rub_1(mocked_get, transactions_USD_1):
    """Положительный тест на работу функции по USD с симуляцией ответа от ресурса"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "date": "2025-03-07",
        "info": {"rate": 89.299623, "timestamp": 1741339623},
        "query": {"amount": 9824.07, "from": "USD", "to": "RUB"},
        "result": 877285.747326,
        "success": True,
    }
    result = convert_currency_to_rub(transactions_USD_1)
    assert result == 877285.75


@patch("requests.get")
def test_convert_currency_to_rub_2(mocked_get, transactions_eur_1):
    """Положительный тест на работу функции по EUR с симуляцией ответа от ресурса"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "date": "2025-03-07",
        "info": {"rate": 96.872028, "timestamp": 1741341183},
        "query": {"amount": 9724.07, "from": "EUR", "to": "RUB"},
        "result": 941990.381314,
        "success": True,
    }
    result = convert_currency_to_rub(transactions_eur_1)
    assert result == 941990.38


def test_convert_currency_to_rub_3(transactions_RUB_1):
    """Положительный тест на работу функции по RUB"""
    result = convert_currency_to_rub(transactions_RUB_1)
    assert result == 43318.34


@patch("requests.get")
def test_convert_currency_to_rub_4(mocked_get, transactions_USD_1):
    """Отрицательный тест на работу функции - код возврата не равен 200"""
    mocked_get.return_value.status_code = 201
    with pytest.raises(Exception):
        convert_currency_to_rub(transactions_USD_1)
