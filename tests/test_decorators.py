import pytest
from src.decorators import log

def test_log_1():
    """Положительный тест декоратора log на вывод в файл"""
    @log("mylog.txt")
    def function_test_1(x, y):
        return x + y

    function_test_1(3, 4)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        record = file.readline()
        assert record == "function_test_1 the result is 7, OK"

def test_log_2(capsys):
    """Положительный тест декоратора log на вывод в консоль"""
    @log()
    def function_test_2(x, y):
        return x + y

    function_test_2(3, 4)
    captured = capsys.readouterr()
    assert captured.out == "function_test_2 the result is 7, OK\n"
