# Time: O(n + m)
# Space: O(c) where n is the number of chars,
# m is the length of the document, and c is the
# number of unique chars in the characters string
def generateDocument(characters, document):
    letters = {}

# Add the chars in characters to letters
# Note the number of time each char occurs
    for i in characters:
        if i not in letters:
            letters[i] = 0

        letters[i] += 1

# Check if the char is in the document string
    for i in document:
        if i not in letters or letters[i] == 0:
            return False

    # Subtract 1 from letters for the used char
        letters[i] -= 1

# Can make the document string based on the
# characters string
    return True
