# given array to find target sum by 2 nums
# Possible solution
# 1. 2-nd array to hold checked num
# 2. Using 2 pointers
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