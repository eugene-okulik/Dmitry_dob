import random

salary_user = input("Напишите ЗП: ")
bonus = random.choice([True, False])
if salary_user.isdigit():
    if bonus:
        salary_user = int(salary_user)
        rand_percent_bonus = random.randint(1, 100)
        print(
            f"{salary_user}, {bonus} - '${int(salary_user + salary_user * rand_percent_bonus / 100)}'"
        )
    else:
        print(f"{salary_user}, {bonus} - '${salary_user}'")
else:
    print("Ожидаю, что Вы введёте целое положительное число")
