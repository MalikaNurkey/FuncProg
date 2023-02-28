#Вводятся имена студентов в одну строчку через пробел.
# На их основе формируется кортеж. Отобразите на экране все
# имена из этого кортежа, которые содержат фрагмент "ва".
# Имена выводятся в одну строку через пробел.

students = tuple(input().split(' '))
print(students)

find = 'ва'
students_with_find = list()
for i in range(len(students)):
    if not students[i].find(find) == -1:
        students_with_find.append(students[i])

print(*students_with_find)