function bubbleSort(arr) {
    let swapped = true;
    for (let i = arr.length; i > 0; i--) {
        swapped = true;
        for (let j = 0; j < i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = false
            }
        }
        if (swapped == true) {
            break
        }
    }
    return arr
}

sorted = bubbleSort([2, 1, 5, 99, 6, 10])
console.log(sorted)