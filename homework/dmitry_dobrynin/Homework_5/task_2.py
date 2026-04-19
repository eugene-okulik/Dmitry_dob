# Первый результат работы программы

string_parsing = 'результат операции: 42'
number_index = string_parsing.index(':') + 2  # можно было бы использовать .rfind(' ')
need_part = string_parsing[number_index:]
print(f'Результат сложения: {int(need_part) + 10}')

# Второй результат работы программы

string_parsing = 'результат операции: 514'
number_index = string_parsing.index(':') + 2
need_part = string_parsing[number_index:]
print(f'Результат сложения: {int(need_part) + 10}')

# Третий результат работы программы

string_parsing = 'результат работы программы: 9'
number_index = string_parsing.index(':') + 2
need_part = string_parsing[number_index:]
print(f'Результат сложения: {int(need_part) + 10}')

# более универсальное
# string_parsing = 'результат работы программы: 9'
# need_part = string_parsing.strip().split()[-1]
# print(f'Результат сложения: {int(need_part) + 10}')
