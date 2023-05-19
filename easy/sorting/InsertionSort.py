# time O(n^2)
# space O(1)
def insertionSort(array):
    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            store = array[i]
            array[i] = array[i + 1]
            array[i + 1] = store
        for j in reversed(range(0, i + 1)):
            if j != 0 and array[j] < array[j - 1]:
                store = array[j]
                array[j] = array[j - 1]
                array[j - 1] = store
    return array


sortedArr = insertionSort([2, 8, 5, 9, 5, 6, 3])
print(sortedArr)

