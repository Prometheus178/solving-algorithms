
# time O(n^2)
# space O(1)
def bubbleSort(array):
    l = 0
    r = len(array) - 1
    while l < r:
        if array[l] > array[l + 1]:
            store = array[l + 1]
            array[l + 1] = array[l]
            array[l] = store

        l += 1
        if l == r:
            l = 0
            r -= 1

    return array


sortedArr = bubbleSort([8, 5, 2, 9, 5, 6, 3])
print(sortedArr)
