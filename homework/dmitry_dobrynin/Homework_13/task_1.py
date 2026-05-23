import os
import datetime
import pathlib

# base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
base_path = pathlib.Path(__file__).parents[3]  #  нашел такой способ простраивания пути
need_path = os.path.join(base_path, "homework/eugene_okulik/hw_13", "data.txt")


def read_files():

    with open(need_path) as data_file:
        for line in data_file:
            yield line


for data_line in read_files():
    time_now = datetime.datetime.now()
    date_data_line = datetime.datetime.strptime(
        " ".join(data_line.split()[1:3]), "%Y-%m-%d %H:%M:%S.%f"
    )
    if "на неделю позже" in data_line.lower():
        print(
            f'Задание было «распечатать эту дату, но на неделю позже», результат: {date_data_line + datetime.timedelta(days=7)}'
        )
    elif "какой это будет день недели" in data_line.lower():
        print(
            f'Задание было «распечатать какой это будет день недели», результат: {date_data_line.strftime("%A")}'
        )
    elif "сколько дней назад была эта дата" in data_line.lower():
        print(
            f'Задание было «распечатать сколько дней назад была эта дата», результат: {(time_now - date_data_line).days}'
        )
    else:
        print('Команда мне такая пока непонятна')
