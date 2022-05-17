# Time: O(n)
# Space: O(n)
def caesarCipherEncryptor(string, key):
    newLetters = []
    newkey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for i in string:
        newLetters.append(getNewLetter(i, newkey, alphabet))
    return "".join(newLetters)


def getNewLetter(i, key, alphabet):
    newLetterCode = alphabet.index(i) + key
    return alphabet[newLetterCode % 26]
