import random


def isSorted(list):
    sorted_list = sorted(list)

    reverse_sorted_list = sorted(list)
    reverse_sorted_list.reverse()

    if list == sorted_list or list == reverse_sorted_list:
        return True
    else:
        return False


size = random.randint(3, 7)
my_list = [random.randint(1, 10) for i in range(size)]

print('Список: ' + str(my_list))
print('isSorted: ' + str(isSorted(my_list)))

print('\nСортировка списка:\n')
my_list.sort()

print('Список: ' + str(my_list))
print('isSorted: ' + str(isSorted(my_list)))

print('\nРазворот списка:\n')
my_list.reverse()

print('Список: ' + str(my_list))
print('isSorted: ' + str(isSorted(my_list)))