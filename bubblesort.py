def bubbleSort(arr):
    swapped = True
    for i in range(len(arr)):
        swapped = True
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = False
        if swapped is True:
            break
    return arr


sorted = bubbleSort([2, 1, 5, 99, 7, 10])
print(sorted)
