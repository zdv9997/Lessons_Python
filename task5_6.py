# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.
import random


def search_num(num, attemp, find):
    if find == True:
        print(f"Вы угадали число {num} ")
        return
    elif find == False and attemp>=10:
        print(f"Попытки закончились. Вы не угадали число {num} ")
        return
    else:
        n = int(input("Введите число: "))
        if n == num:
            print(f"Вы угадали число {num}")
            find = True
            return
        elif n > num:
            print(f"Загаданное число меньше чем {n} ")
            attemp += 1
            return search_num(num, attemp, find)
        else:
            print(f"Загаданное число больше чем {n} ")
            attemp += 1
            return search_num(num, attemp, find)


num = random.randint(0, 100)
search_num(num, attemp=0, find='False')

