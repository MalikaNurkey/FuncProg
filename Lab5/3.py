#Напишите   программу которая   возвращает   список.
# Заранее подготовьте  список  предметов  и  оценок
# учащихся.Когда вы  вводите имя учащегося, то должны отображаться
# оценки этого учащегося.
students = [
    ['Джакс', [['Веб', 78], ['Антикор', 85], ['РМП', 75]]],
    ['Дидар', [['Веб', 45], ['Антикор', 96], ['РМП', 68]]],
    ['Мадина', [['Веб', 85], ['Антикор', 78], ['РМП', 89]]],
    ['Амина', [['Веб', 64], ['Антикор', 69], ['РМП', 65]]],
    ['Азамат', [['Веб', 79], ['Антикор', 57], ['РМП', 52]]],
    ['Малика', [['Веб', 66], ['Антикор', 65], ['РМП', 85]]],
]


def print_student(name):
    index_of_student = None

    for i in range(len(students)):
        if students[i][0] == str(name).capitalize():
            index_of_student = i
            break

    if index_of_student is None:
        print("Такого студента не существует.")
        return

    print('Оценки ученика ' + str(students[i][0]) + ':')
    for i in range(len(students[index_of_student][1])):
        print(str(students[index_of_student][1][i][0]) + ': ' + str(students[index_of_student][1][i][1]) + '%')


name = input('Оценки какого ученика просмотреть: ')
print_student(name)
