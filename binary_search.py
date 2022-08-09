import random


def binary_search(number, arr):
    fst = 0
    lst = len(arr) - 1
    res_found = False
    while fst <= lst and not res_found:
        middle = (fst + lst) // 2
        if number == arr[middle]:
            res_found = True
            return res_found
        if number < arr[middle]:
            lst = middle-1
        if number > arr[middle]:
            fst = middle+1
    return res_found


def sort_random(fst, lst):
    arr = []
    if len(arr) == 0:
        arr.append(fst)
        while arr[len(arr) - 1] < lst:
            arr.append(random.randint(arr[len(arr)-1], lst))
    return arr


arr = sort_random(0, 10)
print(binary_search(8, arr))
print(arr)

