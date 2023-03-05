# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def mult_recursive(a, b):
    if type(a) != int or a < 1 or type(b) != int or b < 1:
        return None
    if b == 0:
        return 1
    if b == 1:
        return a
    # print(a, b)
    return a * mult_recursive(a, b - 1)

input_list = input("Enter two digits divided by space: ").split()
print(mult_recursive(int(input_list[0]), int(input_list[1])))