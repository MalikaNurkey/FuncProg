def add(student, clas):
    list_names.append(student)
    list_class.append(clas)


def show(list_names, list_class):
    for i in range(len(list_names)):
        print(f'Ученик: {list_names[i]}')
        print(f'Класс: {list_class[i]}')


def bubble_sort(nonsort_list, list_names):
    size = len(nonsort_list)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if nonsort_list[j] > nonsort_list[j + 1]:
                nonsort_list[j], nonsort_list[j + 1] = nonsort_list[j + 1], nonsort_list[j]
                list_names[j], list_names[j + 1] = list_names[j + 1], list_names[j]


list_names = []
list_class = []


add('Malika', 11)
add('Daniyarbek', 5)
add('Didar', 9)

print('До сортировки:')
show(list_names, list_class)
print()

print('После сортировки:')
bubble_sort(list_class, list_names)
show(list_names, list_class)