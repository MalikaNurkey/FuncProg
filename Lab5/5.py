numbers = []

while True:
    num = int(input('Введите число: '))
    if not num == 0:
        numbers.append(num)
    else:
        break

numbers.sort()
numbers.reverse()

for num in numbers:
    print(num)