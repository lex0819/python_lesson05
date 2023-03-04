# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_ratings(list_nums):
    # max_item = max(list_nums)
    # min_item = min(list_nums)

    min_item, max_item = sorted(list_nums)[::n-1]
    
    for i, val in enumerate(list_nums):
        if val == max_item:
            list_nums[i] = min_item
    
    return list_nums


n = int(input("Enter lenght of array: "))
list_nums = [int(input("enter each item of array: ")) for _ in range(n)]
print(change_ratings(list_nums))