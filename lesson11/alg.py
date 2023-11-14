import random
import time

def arrRandmizer(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1,1000000))
    return arr

# cортировка пузырьком
def bubleSort(arr):
    for i in range(len(arr)):
        for z in range(len(arr)-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]

# Сортировка вставкой
def mySort(arr):
    for i in range(1, len(arr)):
        while (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

# Шейкерная сортировка
def cocktail_shaker_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        is_swapped = False

        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                is_swapped = True
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True

        if not is_swapped:
            return arr


arr = arrRandmizer(10000)
startTime1 = time.time()
cocktail_shaker_sort(arr)
endTime1 = time.time()
print(f'Сортировка шейкерная {endTime1-startTime1}')

arr = arrRandmizer(10000)
startTime = time.time()
mySort(arr)
endTime = time.time()
print(f'Сортировка вставками {endTime-startTime}')

arr = arrRandmizer(10000)
startTime2 = time.time()
bubleSort(arr)
endTime2 = time.time()
print(f'Сортировка пузырьком {endTime2-startTime2}')