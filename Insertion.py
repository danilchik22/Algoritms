from datetime import datetime
from random import random, randint


def sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


if __name__ == "__main__":
    arr = [34, 12, -345, -25332]
    time1 = datetime.now()
    sort(arr)
    time2 = datetime.now()
    print(time2-time1)
    for _ in range(len(arr)):
        print(arr[_])

