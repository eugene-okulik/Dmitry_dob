#  Первая реализация. Получилось вначале так решить, но я чуть условие поменял

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))


def calc_operation(func):

    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"
        func(first, second, operation)
        print("Операция завершена")

    return wrapper


@calc_operation
def calc(first, second, operation):
    if operation == "+":
        print(first + second)
    elif operation == "-":
        print(first - second)
    elif operation == "/":
        print(first / second)
    elif operation == "*":
        print(first * second)
    elif operation == "**":
        print(first**second)
    else:
        print(
            "Операция нам неизвестна, воспользуйтесь другим калькулятором."
            " Если необходимо вычесть корень квадратный, то возведите в степень 0.5"
        )


calc(first, second, "+")


# Вторая реализация

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))


def calc_operation(func):

    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"
        print(func(first, second, operation))
        print("Операция завершена")

    return wrapper


@calc_operation
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second
    elif operation == "**":
        return first**second
    else:
        return (
            "Операция нам неизвестна, воспользуйтесь другим калькулятором."
            " Если необходимо вычесть корень квадратный, то возведите в степень 0.5"
        )


calc(first, second, ")")
