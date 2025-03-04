import pytest
from src.decorators import log

def test_log():
    """Положительный тест декоратора log на вывод в файл"""
    @log("mylog.txt")
    def function_test_1(x, y):
        return x + y

    function_test_1(3, 4)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        record = file.readline()
        assert record == "function_test_1 OK"


