def getNextIdx(current_idx, array):
    jump = array[current_idx]
    nextIdx = (current_idx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

# Time O(n) | Space O(n)
def hasSingleCycle(array):
    count = 0
    currentIdx = 0
    visited = set()
    while count < len(array):
        currentIdx = getNextIdx(currentIdx, array)
        if visited.__contains__(currentIdx):
            return False
        visited.add(currentIdx)
        count += 1

    return currentIdx == 0


array = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(array))

array1 = [1, -1, 1, -1]
print(hasSingleCycle(array1))

