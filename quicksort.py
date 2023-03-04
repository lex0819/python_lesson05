def quicksort(array):
    if len(array) < 2:
        return array
    else:
        middle = array[0]
        less = [i for i in array[1:] if i <= middle]
        greater = [i for i in array[1:] if i > middle]
    return quicksort(less) + [middle] + quicksort(greater)

n = int(input("Enter lenght of array: "))
inp_list = [int(input("enter each item of array: ")) for _ in range(n)]

print(quicksort(inp_list))