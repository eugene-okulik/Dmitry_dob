# num_user = input("Угадайте цифру, введите целое цисло: ")
# main_num = 4
# while True:
#     if num_user.isdigit():
#         if int(num_user) == main_num:
#             print("Поздравляю! Вы угадали!")
#             break
#         else:
#             num_user = input("Попробуйте снова: ")
#     elif "-" in num_user and num_user.count("-") == 1 and num_user[1:].isdigit():
#         if int(num_user) == main_num:
#             print("Поздравляю! Вы угадали!")
#             break
#         else:
#             num_user = input("Попробуйте снова: ")
#     else:
#         num_user = input("Ввод некорректный, ожидается целое число. Попробуйте снова: ")


# Вторая реализация


main_num = 4
while True:
    num_user = input("Угадайте цифру, введите целое цисло: ")
    if num_user.isdigit():
        if int(num_user) == main_num:
            print("Поздравляю! Вы угадали!")
            break
        else:
            print("Попробуйте снова")
    elif "-" in num_user and num_user.count("-") == 1 and num_user[1:].isdigit():
        if int(num_user) == main_num:
            print("Поздравляю! Вы угадали!")
            break
        else:
            print("Попробуйте снова")
    else:
        print("Ввод некорректный, ожидается целое число. Попробуйте снова")
