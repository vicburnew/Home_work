from logging import exception


def log(filename=""):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Принимает необязательный аргумент
    filename, который определяет, куда будут записываться логи (в файл или в консоль).
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль
    Логирование включает:
    Имя функции и результат выполнения при успешной операции.
    Имя функции, тип возникшей ошибки и входные параметры,
    если выполнение функции привело к ошибке."""

    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{function.__name__} the result is {result}, OK")
                print(f"{function.__name__} the result is {result}, OK")
            except:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{function.__name__} error:{exception.__name__}. Inputs:{args}")
                print(f"{function.__name__} error:{exception.__name__}. Inputs:{args}")
                raise Exception

            return result

        return wrapper

    return decorator
