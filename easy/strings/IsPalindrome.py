# time O(n)
# space O(1)
def isPalindrome(string):
    res = True
    l = 0
    r = len(string) - 1

    while l < len(string) / 2:
        if string[l] != string[r]:
            res = False
        l += 1
        r -= 1
    return res
print(isPalindrome("abcdcba"))
