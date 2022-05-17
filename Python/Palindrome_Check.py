# Time: O(n)
# Space: O(n)
def isPalindrome(string):
    reversedChars = []

    for i in reversed(range(len(string))):
        reversedChars.append(string[i])

    return string == "".join(reversedChars)


# Time: O(n)
# Space: O(1)
def isPalindrome2(string):

    # Initialize the left index to the first element in the string
    # Initialize the right index to the last element in the string
    leftIdx = 0
    rightIdx = len(string) - 1

    # While the left index is less than the right index, continue
    while leftIdx < rightIdx:

        # If the left index value does not equal the right index value, return false
        if string[leftIdx] != string[rightIdx]:
            return False

    # Otherwise increment the left index by one and decrement the right index by one
        leftIdx += 1
        rightIdx -= 1

    # Return true because the string is a palindrome
    return True
