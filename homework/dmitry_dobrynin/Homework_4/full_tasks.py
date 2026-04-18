my_dict = {"tuple": ("Sochi", "Omsk", "Moscow", "Novosibirsk", "Samara", True),
           "list": ["PM", "Dev", "QA", "PO", "UI/UX", None], 
           "dict": {"first_name": "Dmitry",
                    "middle_name": "Victorovich",
                    "last_name": "Dobrynin",
                    "city": "Krasnoyarsk",
                    "age": 27,
                    "salary": 123_567.89
                    }, 
           "set": {"Russia", "Germany", "Georgia", "China", "USA"}
           }

# Задание 1

print(my_dict['tuple'][-1])

# Задание 2

my_dict['list'].append('Автоматизация')
my_dict['list'].pop(1) # выбрал единицу, потому что второй элемент находится под индексом 1

# Задание 3

my_dict['dict']['i am a tuple'] = 'Good'
my_dict['dict'].pop('middle_name')

# Задание 4

my_dict['set'].add('Japan')
my_dict['set'].pop() # удаляю случайный элемент из множества
random_list = list(set([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])) # удаляю дубликаты из списка с помощью множества

# Итог 

print(my_dict)