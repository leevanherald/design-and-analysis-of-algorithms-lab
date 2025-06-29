def length_of_LIS(nums):
    n = len(nums)
    seq = []  # Stores the piles
    parent = [-1] * n  # Tracks the previous index in the LIS
    pos = [-1] * n  # Stores the last index of the LIS ending at each pile

    # Create the first pile
    seq.append(nums[0])
    pos[0] = 0
    lis_end = 0  # Tracks the last index of LIS

    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # Go through each card
    for j in range(1, n):
        # Find the left-most pile that can accommodate this card
        idx = binary_search(seq, nums[j])

        if idx == len(seq):
            # If no such pile exists, create a new pile
            seq.append(nums[j])
            pos[idx] = j
            parent[j] = pos[idx - 1] if idx > 0 else -1
            lis_end = j  # Update LIS end only if we extend LIS
        else:
            # If a pile is found, place this card on top of that pile
            seq[idx] = nums[j]
            pos[idx] = j  # Update position
            parent[j] = pos[idx - 1] if idx > 0 else -1

            # Update lis_end if we replace the last element
            if idx == len(seq) - 1:
                lis_end = j

        print(seq)
    # Reconstruct the LIS sequence
    lis = []
    k = lis_end
    while k != -1:
        lis.append(nums[k])
        k = parent[k]

    lis.reverse()

    print("Longest Increasing Subsequence:", lis)
    return len(seq)


# Example usage
nums = [0, 1, 10, 6, 7, 2, 3]
print("Length of LIS:", length_of_LIS(nums))
