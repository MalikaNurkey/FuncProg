#Общий объем расходов. Разработайте программу, которая
# подсчитает ваши расходы за каждый день недели.Расходы
# по следующим категориям(транспортные расходы, обед, ит.д.)
# Суммы должны быть сохранены в списке. Примените цикл, чтобы
# вычислить общий объем расходов занеделю и показать результат.

transport = [80, 120, 80, 80, 120, 200, 200]
food = [1900, 1000, 300, 1900, 0, 300, 3000]
other = [1000, 1920, 310, 1500, 250, 1020, 55000]


def spending(transport, food, other):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    general = 0
    spending_list = list()
    for i in range(7):
        sum = transport[i] + food[i] + other[i]
        spending_list.append(tuple([days[i], sum]))
        general += sum

    spending_list.append(tuple(['Общий', general]))
    return spending_list


def spend_print(spending):
    for i in range(len(spending)):
        print(f'{spending[i][0]}: {spending[i][1]} тенге.')


spend_tuple = spending(transport, food, other)
spend_print(spend_tuple)