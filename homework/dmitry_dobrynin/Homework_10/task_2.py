# первая часть задания


def repeat_me(func):

    def wrapper(text, count):
        for _ in range(count):
            func(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example("print me", count=2)


# вторая часть задания


def repeat_me(count):

    def decorator(func):
        def wrapper(text):
            for _ in range(count):
                func(text)

        return wrapper

    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example("print me")
