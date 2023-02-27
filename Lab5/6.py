import random


numbers = set()
while len(numbers) < 6:
    numbers.add(random.randint(1,49))

numbers = sorted(list(numbers))

for num in numbers:
    print(num)