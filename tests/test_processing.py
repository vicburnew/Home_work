import pytest

from src.processing import filter_by_state


# Тестирование функции filter_by_state

def test_filter_by_state_posit_1(list_of_dict_fixt_initial, list_of_dict_fixt_executed):
    """Положительное тестирование с использованием фикстур, флаг = EXECUTED"""
    assert filter_by_state(list_of_dict_fixt_initial) == list_of_dict_fixt_executed

def test_filter_by_state_posit_2(list_of_dict_fixt_initial, list_of_dict_fixt_cancel):
    """Положительное тестирование с использованием фикстур, флаг = CANCELED"""
    assert filter_by_state(list_of_dict_fixt_initial, "CANCELED") == list_of_dict_fixt_cancel

def test_filter_by_state_posit_3(list_of_dict_fixt_no_state):
    """Отрицательное тестирование с использованием фикстур, частичное отсутствие флагов"""
    with pytest.raises(ValueError):
        filter_by_state(list_of_dict_fixt_no_state)


