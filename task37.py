# Задача №37. Решение в группах 15 минут
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def revers_string(n):
    if n == 1:
        return input()
    n -= 1
    temp = revers_string(n)
    return input() + " " + temp

print(revers_string(int(input("enter nunbers: "))))


from random import randrange
def revers_samodur(n):
    if n == 0:
        return "\n"
     
    print(random_input := randrange(n), end=" ")
    return f"{revers_samodur(n - 1)} {random_input}"

print(revers_samodur(int(input("enter n: "))))
