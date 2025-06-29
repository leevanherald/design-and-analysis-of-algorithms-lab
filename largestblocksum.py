def brute_sum(arr, n):
    max_sum = arr[0]
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

def kadane_sum(arr, n):
    max_sum = arr[0]
    current_max = arr[0]
    
    for i in range(1, n):
        current_max = max(current_max + arr[i], arr[i])
        max_sum = max(max_sum, current_max)
    
    return max_sum


n = 7
arr = [2, 3, -8, 7, -1, 2, 3]

print("Maximum Block Sum Brute:", brute_sum(arr, n))
print("Maximum Block Sum Kadane:", kadane_sum(arr, n))