# Time: O(n)
# Space: O(1)
def isValidSubsequence(array, sequence):
    idx = 0

    for i in array:
        if idx == len(sequence):
            break

        if sequence[idx] == i:
            idx += 1

    return idx == len(sequence)
