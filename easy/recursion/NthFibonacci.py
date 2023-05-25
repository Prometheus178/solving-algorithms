# 0 1 1 2 3 5 8 13 21

# time O(2^n)
# space O(n)
# too many unnecessary count
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n - 2) + getNthFib(n - 1)


print(getNthFib(7))
