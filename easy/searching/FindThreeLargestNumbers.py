# time O(n)
# space O(1)
def findThreeLargestNumbers(array):
    res = [None, None, None]
    for num in array:
        if res[2] is None or num > res[2]:
            shiftUpdate(res, num, 2)
        elif res[1] is None or num > res[1]:
            shiftUpdate(res, num, 1)
        elif res[0] is None or num > res[0]:
            shiftUpdate(res, num, 0)

    return res


def shiftUpdate(res, num, idx):
    for i in range(0, idx + 1):
        if i == idx:
            res[i] = num
        else:
            res[i] = res[i + 1]


res = findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
print(res)
