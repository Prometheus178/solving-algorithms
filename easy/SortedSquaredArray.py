# Return ascending ordered Squared input array

# time O(n + n * log(n)) or O(n log(n))
# space O(n)
def sortedSquaredArray(array):
    sqared = []
    for i in range(len(array)):
        sq = array[i] * array[i]
        sqared.append(sq)
    sqared.sort()
    return sqared


array = sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])
array2 = sortedSquaredArray([100, 50, 65, 82, 23])
print(array)
print(array2)
