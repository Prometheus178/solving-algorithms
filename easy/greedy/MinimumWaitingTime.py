def minimumWaitingTime(queries):
    queries.sort()
    count = 0
    l = 0
    print(queries)
    for n in queries:
        count += l
        l += n
    return count


waiting_time = minimumWaitingTime([3, 2, 1, 2, 6])
print(waiting_time)
