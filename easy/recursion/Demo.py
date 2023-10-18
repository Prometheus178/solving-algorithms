# 0 , 1 , 4 , 9 , 16 , 25   = 55
def sum(n):
    print(n)
    sq = n * n
    # print(sq)
    if n == 0:
        return sq
    return sq + countSum(n - 1)


# print(sum(5))

def rec(n, store, visited):
    if n == 0:
        return visited
    print("level: " + str(n))
    print(visited)
    n = 0
    if (len(store) != 0):
        n = store.pop()
    visited.append(n)
    return rec(n, store, visited)


def begin(n, visited):
    store = list()
    i = 1
    while (i <= n):
        store.append(i)
        i = i + 1
    rec(n, store, visited)


# function to calculate the sum of all the numbers from 1 to n
def countSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
        print(sum)
    print(sum)


countSum(10)
