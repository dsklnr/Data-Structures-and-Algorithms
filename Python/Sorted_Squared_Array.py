# Time: O(n log(n))
# Space: O(n)
def sortedSquaredArray(array):
    ans = []

    for i in array:
        x = i * i
        ans.append(x)

    ans.sort()
    return ans


# Time: O(n)
# Space: O(n)
def sortedSquaredArray2(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares
