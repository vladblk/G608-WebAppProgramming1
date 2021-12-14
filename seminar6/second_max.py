n = int(input('n: '))
input_arr = input('grades: ').split(' ')
second_max_grade = sorted(list(set(map(int, input_arr))))[-2]

print(second_max_grade)
