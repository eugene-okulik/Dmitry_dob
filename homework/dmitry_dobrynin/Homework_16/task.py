from pathlib import Path
import os
import mysql.connector as mysql
import csv
from dotenv import load_dotenv
load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)
base_path = Path(__file__)
need_path = base_path.parents[2]
file_path = os.path.join(
    need_path, "eugene_okulik/Lesson_16/hw_data", "data.csv"
)

cursor = db.cursor()
query = '''
SELECT s.name,
       s.second_name,
       g.title as group_title,
       b.title as book_title,
       s2.title as subject_title,
       l.title as lesson_title,
       m.value as mark_value
FROM students s
JOIN `groups` g on g.id = s.group_id
JOIN books b on b.taken_by_student_id = s.id
JOIN marks m on m.student_id = s.id
JOIN lessons l on l.id = m.lesson_id
JOIN subjects s2 on s2.id = l.subject_id
WHERE s.name = %s AND
      s.second_name = %s AND
      g.title = %s AND
      b.title = %s AND
      s2.title = %s AND
      l.title = %s AND
      m.value = %s
'''

with open(file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    next(file_data)
    for value in file_data:
        cursor.execute(query, value)
        result = cursor.fetchall()
        if len(result) == 0:
            print(value)

cursor.close()
db.close()
