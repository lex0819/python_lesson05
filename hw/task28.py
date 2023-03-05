# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum_recursive(a, b):
    if type(a) != int or a < 0 or type(b) != int or b < 0:
        return None
    if b == 0:
        return a
    return sum_recursive(a + 1, b - 1)

input_list = input("Enter two digits divided by space: ").split()
print(sum_recursive(int(input_list[0]), int(input_list[1])))