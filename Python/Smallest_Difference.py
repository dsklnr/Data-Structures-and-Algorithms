# Time: O(n log(n) + m log(m))
# Space O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallestNum = float("inf")
    current = float("inf")
    ans = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1

        elif firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1

        else:
            return [firstNum, secondNum]

        if smallestNum > current:
            smallestNum = current
            ans = [firstNum, secondNum]

    return ans
