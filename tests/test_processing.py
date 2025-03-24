import pytest

from src.processing import filter_by_state, sort_by_date

# Тестирование функции filter_by_state


def test_filter_by_state_posit_1(list_of_dict_fixt_initial, list_of_dict_fixt_executed):
    """тестирование с использованием фикстур, флаг = EXECUTED"""
    assert filter_by_state(list_of_dict_fixt_initial) == list_of_dict_fixt_executed


def test_filter_by_state_posit_2(list_of_dict_fixt_initial, list_of_dict_fixt_cancel):
    """тестирование с использованием фикстур, флаг = CANCELED"""
    assert filter_by_state(list_of_dict_fixt_initial, "CANCELED") == list_of_dict_fixt_cancel




# Тестирование функции sort_by_date


def test_sort_by_date_positive_ascending(list_of_dict_fixt_initial, list_of_dict_fixt_date_sort_asc):
    """тестирование с использованием фикстур по возрастанию дат"""
    assert sort_by_date(list_of_dict_fixt_initial, False) == list_of_dict_fixt_date_sort_asc


def test_sort_by_date_positive_descending(list_of_dict_fixt_initial, list_of_dict_fixt_date_sort_desc):
    """тестирование с использованием фикстур по убыванию дат"""
    assert sort_by_date(list_of_dict_fixt_initial) == list_of_dict_fixt_date_sort_desc


def test_sort_by_date_positive_equaldates_asc(
    list_of_dict_fixt_equaldates_initial, list_of_dict_fixt_equaldates_sort_asc
):
    """тестирование с использованием фикстур при наличии одинаковых дат"""
    assert sort_by_date(list_of_dict_fixt_equaldates_initial, False) == list_of_dict_fixt_equaldates_sort_asc


def test_sort_by_date_positive_equaldates_desc(
    list_of_dict_fixt_equaldates_initial, list_of_dict_fixt_equaldates_sort_desc
):
    """тестирование с использованием фикстур при наличии одинаковых дат"""
    assert sort_by_date(list_of_dict_fixt_equaldates_initial) == list_of_dict_fixt_equaldates_sort_desc

def test_filter_by_currency_2():
    pass

def test_filter_by_currency_3():
    pass


