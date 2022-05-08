# Time: O(n)
# Space: O(n)
def twoNumberSum(array, targetSum):
    nums = {}

    for i in array:
        result = targetSum - i

        if result in nums:
            return [result, i]
        else:
            nums[i] = True

    return []

# Time: O(nlog(n))
# Space: O(1)
def twoNumberSum2(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == targetSum:
            return [array[left], array[right]]
        
        elif sum < targetSum:
            left += 1

        elif sum > targetSum:
            right -= 1

    return []