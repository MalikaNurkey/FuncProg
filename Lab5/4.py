numbers = []

while True:
    num = int(input('Введите число: '))
    if not num == 0:
        numbers.append(num)
    else:
        break

numbers.sort()

for num in numbers:
    print(num)