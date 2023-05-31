# time O(n^m) where m is count of array layers inside
# space O(1)

def productSum(array):
    return count(1, array)


def count(n, array):
    res = 0
    i = 0
    while i < len(array):
        val = array[i]
        if isinstance(val, int):
            res = res + val
        else:
            val = count(n + 1, val)
            res = res + val
        i += 1
    return n * res


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
