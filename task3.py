# Задание 3.

# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

num = input("Введите целое число: ")
summ = int(num) \
       + int(num + num) \
       + int(num + num + num)

print(f"Сумма равна: {summ}")