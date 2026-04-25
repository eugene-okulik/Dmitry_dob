temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

# первая часть задания

new_list = list(filter(lambda day: day > 28, temperatures))
print(new_list)

# вторая часть задания


def print_day_stat_temperature(arg):
    print(f'Самая высокая температура: {max(arg)}')
    print(f'Самая низкая температура: {min(arg)}')
    print(f'Средняя температура: {round(sum(arg) / len(arg))}')


print_day_stat_temperature(new_list)
