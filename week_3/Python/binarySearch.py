import matplotlib.pyplot as plt
import time


def binarySearch(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, left, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, right, x)
    else:
        return -1


numbers = list()
times = list()

for i in range(1, 11):
    t = 0;
    #     for j in range(1,31):
    a = list(range(1, 10000000 * i + 1))
    start = time.process_time()
    result = binarySearch(a, 0, len(a) - 1, 1)
    end = time.process_time()
    t += end - start

    numbers.append(len(a))
    times.append(t)

plt.plot(numbers, times)
plt.xlabel('Số lượng phần tử trong dãy')
plt.ylabel('Thời gian chạy')
plt.grid()
plt.show()
