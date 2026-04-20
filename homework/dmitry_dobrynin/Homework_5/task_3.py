students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(
    f'Students {students[0]}, {students[1]}, {students[2]} '
    f'study these subjects: {subjects[0]}, {subjects[1]}, {subjects[2]}'
)

# либо

print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
