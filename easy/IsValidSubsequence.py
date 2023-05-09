# to find ordered subsequence in 1st array

# time O(n)
# space O(1)
def isValidSubsequence(array, sequence):
    if len(sequence) == 0:
        return False

    r = 0
    for l in array:
        if r < len(sequence) and l == sequence[r]:
            r += 1
    return r == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))
