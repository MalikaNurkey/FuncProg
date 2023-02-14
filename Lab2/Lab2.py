student = "Нуркей Малика"
course1 = "Анализ данных"
course2 = "Функ. программирование"
course3 = "Веб программирование"
course4 = "Операционные системы"
#Вывод информации про студента
print("Студент:" + student)
print("Дисципины:" + course1 + ", " + course2 + ", " + course3 + ", " + course4)
#Выбор дисциплины для просмотра балла
course = input("Выберите дисциплину:")
if course == course1:
    print(75)
elif course == course2:
    print(83)
elif course == course3:
    print(91)
elif course == course4:
    print(80)
#Если ввод был неправьный, то выйдет ошибка
else: print("ERROR")