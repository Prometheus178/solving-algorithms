def getNextIdx(current_idx, array):
    jump = array[current_idx]
    nextIdx = (current_idx + jump) % len(array)
    return nextIdx


def hasSingleCycle(array):
    count = 0
    currentIdx = 0

    while count < len(array):
        currentIdx = getNextIdx(currentIdx, array)
        count += 1

    return currentIdx == 0


array = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(array))
