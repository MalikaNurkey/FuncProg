#Создайте кортеж-матрешку, в который поместите два элемента:
# целое число и вложенный кортеж, в который поместите еще два
# элемента: вещественное число и вложенный кортеж, в который
# поместите еще два элемента: комплексное число и вложенный
# кортеж, в который поместите еще два элемента: строку и
# пустой кортеж. Выведите на экран конечную строку.

matryoshka = (
    (11, (11.119,(complex(1),('String', ())))),
)
print(matryoshka)