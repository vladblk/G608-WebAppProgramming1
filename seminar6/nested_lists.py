n = int(input('num of students: '))
all_students = []

for i in range(n):
    name = input('name: ')
    grade = float(input('grade: '))
    all_students.append([name, grade])

all_grades = []

for i in all_students:
    all_grades.append(i[1])

second_lowest_grade = sorted(list(set(all_grades)))[1]
print(second_lowest_grade)

names = []

for i in all_students:
    if i[1] == second_lowest_grade:
        names.append(i[0])

print(sorted(names))