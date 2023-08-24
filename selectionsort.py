def selectionSort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
        return arr


sorted_array = selectionSort([2, 1, 5, 99])
print(sorted_array)
