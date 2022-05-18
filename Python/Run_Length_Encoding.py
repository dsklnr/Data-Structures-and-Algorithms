# Time: O(n)
# Space: O(n)
def runLengthEncoding(string):
    # Initialize chars and number of chars
    chars = []
    currentRun = 1

    # Loop through the string and count the number of times
    # the same char occurs in a row
    for i in range(1, len(string)):
        currentChar = string[i]
        previousChar = string[i - 1]

        if currentChar != previousChar or currentRun == 9:
            chars.append(str(currentRun))
            chars.append(previousChar)
            currentRun = 0

        currentRun += 1

    # Handle the last char in the string
    chars.append(str(currentRun))
    chars.append(string[len(string) - 1])

    # Return the final string
    return "".join(chars)
