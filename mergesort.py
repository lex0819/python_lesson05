def merge_sort(numbers):
    if len(numbers) > 1:
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

n = int(input("Enter lenght of array: "))
list_nums = [int(input("enter each item of array: ")) for _ in range(n)]
merge_sort(list_nums)
print(list_nums)