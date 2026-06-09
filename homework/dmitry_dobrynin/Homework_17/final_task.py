import argparse
import pathlib
import datetime
from colorama import init, Fore
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Название файла")
parser.add_argument("-d", "--date", help="Дата поиска")
parser.add_argument("-t", "--text", help="Уровень лога", required=True)
parser.add_argument("-f", "--full", help="Объем лога", action="store_true")
args = parser.parse_args()


def definition_path():
    if args.file.endswith(".log"):
        return [args.file]
    else:
        return list(pathlib.Path(args.file).glob("*.log"))


base_path = definition_path()


def is_new_block(line):
    try:
        datetime.datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S.%f')
        return True
    except ValueError:
        return False


def read_file(file):
    new_block = ''
    start_line = 1
    with open(file, 'r') as data_file:
        for counter_line, line in enumerate(data_file, start=1):
            if is_new_block(line):
                if new_block:
                    # отдаю старый блок и номер строки
                    yield new_block, start_line
                # начинаю новый блок
                new_block = line
                start_line = counter_line
            else:
                new_block += line
        if new_block:
            yield new_block, start_line


# оставил full_block, т.к в условиях задания есть такое требование
full_block = dict()  # хотя не использую
found = False

for file in base_path:
    for data_block, counter_line in read_file(file):
        if args.date and args.date not in data_block[:10]:
            continue
        full_block[data_block[:23]] = data_block
        if args.text in data_block:
            found = True
            part_data = data_block.split()
            index_error = part_data.index(args.text)
            print("В файле: " + Fore.BLUE + f"{file}"
                  + Fore.RESET + " найден необходимый уровень лога")
            print("Дата и Время:" + Fore.BLUE + f"{data_block[:23]}")
            print("Cтрока: " + Fore.BLUE + f"{counter_line}")
            print("До слова - "
                  + Fore.BLUE + f"{' '.join(part_data[:index_error])}"
                  + Fore.RED + f" [{args.text}] "
                  + Fore.RESET + "После слова - "
                  + Fore.BLUE
                  + f"{' '.join(part_data[index_error + 1:index_error + 6])}")
            print(Fore.GREEN + "-" * 49)
            if not args.full:
                break

if not found:
    print('Данный уровень лога не найден.'
          ' Убедитесь, что искали по точному слову.')
