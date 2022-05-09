# Time: O(n log(n))
# Space: O(1)
def nonConstructibleChange(coins):
    coins.sort()
    totalCoins = 0

    for i in coins:
        if i > totalCoins + 1:
            return totalCoins + 1

        totalCoins += i

    return totalCoins + 1
