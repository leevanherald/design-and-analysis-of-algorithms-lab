# function to return the majority element in an array
# Brute force method
# Sorting method
# Boyer Moore voting algorithm
def majority_element_brute_force(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count = count + 1
        if count > n / 2:
            return nums[i]
    return -1


def sorting_based_majority(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    nums.sort()
    count = 1

    for i in range(1, n):
        if nums[i-1] == nums[i]:
            count = count + 1
        else:
            if count > n // 2:
                return nums[i-1]
            count = 1

    if count > n // 2:
        return nums[-1]

    return -1


def boyer_moore_voting(nums):
    count = 0
    candidate = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        if num == candidate:
            count = count + 1
        else:
            count = count - 1

    # Validate the canidate
    for num in nums:
        if num == candidate:
            count = count + 1

    if count > len(nums) // 2:
        return candidate
    else:
        return -1


# Test the function
array = [1, 1, 2, 1, 3, 5, 1]
# ans = majority_element_brute_force(array)

# ans = sorting_based_majority(array)
ans = boyer_moore_voting(array)
print(ans)
