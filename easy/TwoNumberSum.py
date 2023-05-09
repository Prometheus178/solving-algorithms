# given array to find target sum by 2 nums
# Possible solution
# 1. Using 2 pointers
# 2. 2-nd store in HashTable with time complexity O(1) to hold checked num

# time O(n^2)
# space O(1)
def twoNumberSum(array, targetSum):
    result = []
    l = 0
    r = 1
    arr_len = len(array) - 1
    while l < arr_len:
        a = array[l]
        c = targetSum - a
        while r <= arr_len:
            b = array[r]
            if b == c:
                result.append(a)
                result.append(b)
                break
            r += 1
        l += 1
        r = l + 1
    return result


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))


# time O(N)
# space O(N)
def twoNumberSum2(array, targetSum):
    checked = set()
    res = []
    for x in array:
        c = targetSum - x
        if c in checked:
            res.append(c)
            res.append(x)
        else:
            checked.add(x)
    return res

print(twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10))
