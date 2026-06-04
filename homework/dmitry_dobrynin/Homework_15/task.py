import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port="25060",
    database="st-onl",
)

cursor = db.cursor(dictionary=True)

#   "Создайте студента (student)"
query = """
INSERT INTO students(name, second_name)
VALUES (%s, %s)
"""
values = ("Илья", "Воеводин")
cursor.execute(query, values)
user_id = cursor.lastrowid  # записываю id пользователя

#  "Создайте несколько книг (books) и укажите,
#   что ваш созданный студент взял их"
query = """
INSERT INTO books(title)
VALUES (%s)
"""
values = [
    ("Братья Карамазовы. Достоевский",),
    ("Мастер и Маргарита. Булгаков",)
]
cursor.executemany(query, values)

db.commit()

query = """
UPDATE books b
SET taken_by_student_id = %s
WHERE b.title IN (%s, %s)
"""
values = (
    user_id,
    "Братья Карамазовы. Достоевский",
    "Мастер и Маргарита. Булгаков"
)
cursor.execute(query, values)

db.commit()

#  "Создайте группу (group) и определите своего студента туда"
query = """
INSERT INTO `groups`(title, start_date)
VALUES (%s, now())
"""
values = ("Группа 1",)
cursor.execute(query, values)
id_group = cursor.lastrowid  # заисываю id группы

db.commit()

query = """
UPDATE students
SET group_id = %s
WHERE id = %s
"""
values = (id_group, user_id)
cursor.execute(query, values)

db.commit()

#  "Создайте несколько учебных предметов (subjects)"

query = """
INSERT INTO subjects(title)
VALUES (%s)
"""
subjects = [("life",), ("informatics",)]
id_subjects = []
for values in subjects:
    cursor.execute(query, values)
    id_subjects.append(cursor.lastrowid)

db.commit()

#  Создайте по два занятия для каждого предмета (lessons)

query = """
INSERT INTO lessons(title, subject_id)
VALUES (%s, %s)
"""
lessons = ['lesson_1', 'lesson_2']
id_lessons = list()
for id in id_subjects:
    for lesson in lessons:
        values = (lesson, id)
        cursor.execute(query, values)
        id_lessons.append(cursor.lastrowid)

db.commit()

#   "Поставьте своему студенту оценки (marks) для всех созданных вами занятий"

query = """
INSERT INTO marks(value, lesson_id, student_id)
VALUES (%s, %s, %s)
"""
values = [
    (4, id_lessons[0], user_id),
    (3, id_lessons[1], user_id),
    (5, id_lessons[2], user_id),
    (5, id_lessons[3], user_id)
]
cursor.executemany(query, values)
db.commit()

#  "Все оценки студента"

query = """
SELECT m.value,
       s.name,
       s.second_name
FROM marks m
JOIN students s on s.id = m.student_id
WHERE s.id = %s
"""
values = (user_id,)
cursor.execute(query, values)
result = cursor.fetchall()
for grade in result:
    print(
        f"Фамилия студента: {grade['second_name']} \n"
        f"Имя студента: {grade['name']} \n"
        f"Оценка: {grade['value']}"
    )


#   Все книги, которые находятся у студента

query = """
SELECT b.title
FROM books b
JOIN students s on s.id = b.taken_by_student_id
WHERE s.id = %s
"""
values = (user_id,)
cursor.execute(query, values)
result = cursor.fetchall()
for book in result:
    print(f"Книга: {book['title']}")


#   Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
#   оценки с названиями занятий и предметов
#   (всё одним запросом с использованием Join)

query = """
SELECT s.id AS student_id, s.name, s.second_name,
       g.id AS group_id, g.title AS group_title,
       b.id AS book_id, b.title AS book_title,
       m.id AS mark_id, m.value AS mark_value,
       l.id AS lesson_id, l.title AS lesson_title,
       s2.id AS subject_id, s2.title AS subject_title
FROM students s
JOIN `groups` g on g.id = s.group_id
JOIN books b on b.taken_by_student_id = s.id
JOIN marks m on m.student_id = s.id
JOIN lessons l on l.id = m.lesson_id
JOIN subjects s2 on s2.id = l.subject_id
WHERE s.id = %s
"""
values = (user_id,)
cursor.execute(query, values)
result = cursor.fetchall()
for info in result:
    for keys, values in info.items():
        print(f"{keys}: {values}")
    print("Cтрока завершена")

cursor.close()
db.close()
