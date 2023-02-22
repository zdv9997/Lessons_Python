# Задание 3. Сформировать из введенного числа
# обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# Пока все числа не извлечены рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все цифры извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число, которое требуется перевернуть: 123
# Перевернутое число: 321
# Не забудьте проверить на числе, которое оканчивается на 0.
# 1230 -> 0321

def replace(num, str_1):
    if num == 0:
        return str_1
    temp_num = str(num % 10)
    str_1 = str_1 + temp_num
    num = int(num / 10)
    return replace(num, str_1)


try:
    num = int(input("Введите целое число: "))
    new_num = replace(num, str_1='')
    print(new_num)
except ValueError:
    print("Надо вводить число... ")

# str_1='1'
# temp_num = str(123 % 10)
# str_1=str_1+temp_num
# print(str_1)