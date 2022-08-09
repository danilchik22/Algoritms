import datetime
import random


def sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


if __name__ == "__main__":
    arr = [random.randint(0, 1000) for _ in range(0, 10000)]
    time1 = datetime.datetime.now()
    sort(arr)
    time2 = datetime.datetime.now()
    print(time2-time1)
    for _ in range(len(arr)):
        print(arr[_])

