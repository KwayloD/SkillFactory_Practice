def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
target = int(input("Введите любое число: "))

for i in range(len(array)):                                  #Сортировка пузырьком
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

position = binary_search(array, target)

if position >= 0:
    print(f"Число {target} должно находиться между числами {array[position-1]} и {array[position+1]}")
else:
    print("Число не найдено в последовательности")