n = int(input('number of students: '))

# name 30 30 30

catalog = {}

for i in range(n):
    student_info = input().split()
    name = student_info[0]
    marks = []
    for mark in student_info[1:len(student_info)]:
        marks.append(float(mark))
    catalog[name] = marks

student_name = input('Student name: ')
student_marks = catalog[student_name]
average_mark = 0

for mark in student_marks:
    average_mark += mark

average_mark = average_mark / len(student_marks)

print(f"Student {student_name} has obtained a {average_mark} average.")
