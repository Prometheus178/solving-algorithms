# 0 , 1 , 4 , 9 , 16 , 25   = 55
def sum(n):
    print(n)
    sq = n * n
    # print(sq)
    if n == 0:
        return sq
    return sq + sum(n - 1)


print(sum(5))
