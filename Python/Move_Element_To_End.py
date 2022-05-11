# Time: O(n)
# Space: 0(1)
def moveElementToEnd(array, toMove):
    for i in array:
        if i == toMove:
            array.remove(i)
            array.append(i)
            i += 1

    return array


# Time: O(n)
# Space: O(1)
def moveElementToEnd2(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:
        while leftIdx < rightIdx and array[rightIdx] == toMove:
            rightIdx -= 1

        if array[leftIdx] == toMove:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        leftIdx += 1

    return array
