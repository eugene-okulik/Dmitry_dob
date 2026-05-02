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
        result = func(first, second, operation)
        if result is not None:
            print(result)

    return wrapper


@calc_operation
def calc_second(first, second, operation):
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


calc_second(first, second, "+")


@calc_operation
def calc_first(first, second, operation):
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


calc_first(first, second, "+")
