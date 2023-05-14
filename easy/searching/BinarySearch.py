# time O(Log n)
# space O(1)
def binarySearch(array, target):
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = l + r // 2
        mVal = array[mid]
        if mVal == target:
            return mVal
        elif target < mVal:
            r = mid - 1
        else:
            l = mid + 1
    return -1


res = binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)
print(res)
res = binarySearch([1, 5, 23, 111], 111)
print(res)
