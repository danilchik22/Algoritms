def sort(arr):
    if len(arr) <= 1:
        return arr
    middle = arr[0]
    left = list(filter(lambda x: x < middle, arr))
    right = list(filter(lambda x: x > middle, arr))
    mid = list(i for i in arr if i == middle)
    return sort(left) + mid + sort(right)


print(sort([34, 12, 2, 23, 13, 1009, 23]))