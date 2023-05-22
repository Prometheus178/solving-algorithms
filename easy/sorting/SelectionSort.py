def selectionSort(array):
    r = len(array) - 1
    l = 0
    i = l
    min = l
    while l < r:
        if array[min] > array[i]:
            min = i
        if i == r:
            print("l: " + str(l))
            print("min: " + str(min))
            swap(l, min, array)
            print(array)
            print("---")
            l += 1
            i = l
        i += 1
    return array


def swap(i, j, array):
    store = array[j]
    array[j] = array[i]
    array[i] = store


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
