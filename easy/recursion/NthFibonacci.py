# 0 1 1 2 3 5 8 13 21

# time O(2^n)
# space O(n)
# too many unnecessary count
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)


print(getNthFib(5))


# time O(n)
# space O(n)
def getNthFibWithStoring(n):
    store = {1: 0, 2: 1}
    return getNthFib(n, store)


def getNthFib(n, store):
    if n in store:
        return store[n]

    store[n] = getNthFib(n - 1, store) + getNthFib(n - 2, store)
    return store[n]


print(getNthFibWithStoring(5))
