function selectionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let smallest = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[smallest]) {
                smallest = j;
            }
        }
        let temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;
    }
    return arr;
}

selectionSort([2, 1, 5, 99, 7, 8])