# Задание 4.

# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

expenses = int(input("Введите затраты предприятия: "))
revenue = int(input("Введите выручку предприятия: "))
profit = revenue-expenses

if profit > 0:
    profitability = float(revenue / expenses)
    staff = int(input("Введите количество сотрудников "))
    profit_staff = float(revenue / staff)

    print(f"Предприятие получило прибыло: {profit}")
    print(f"Рентабельность предприятия: {round(profitability, 2)}")
    print(f"Прибыль на одного сотрудника составляет: {round(profit_staff, 2)}")

elif revenue < expenses:
    profitability = float(revenue / expenses)

    print(f"Предприятие получило убыток: {revenue - expenses}")

else:
    print("Предприятие не имеет прибыли и убыткове")