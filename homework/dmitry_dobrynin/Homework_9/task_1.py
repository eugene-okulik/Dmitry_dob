import datetime

task_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(task_date, "%b %d, %Y - %H:%M:%S")
print(datetime.datetime.strftime(python_date, "Полное название месяца - %B"))
print(datetime.datetime.strftime(python_date, "%d.%m.%Y, %H:%M"))
