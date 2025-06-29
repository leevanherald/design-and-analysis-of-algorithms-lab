def k_way_merge_sort(arr, left, right, k):
    if left < right:
        size = right - left + 1
        part_size = max(1, size // k)  # Ensure part_size is at least 1
        indices = [
            left + i * part_size for i in range(k) if left + i * part_size <= right] + [right + 1]

        for i in range(len(indices) - 1):
            k_way_merge_sort(arr, indices[i], indices[i + 1] - 1, k)

        k_way_merge(arr, indices, len(indices) - 1)


def k_way_merge(arr, indices, k):
    temp = []
    pointers = indices[:-1]

    while True:
        min_index = -1
        min_value = float('inf')
        for i in range(k):
            if pointers[i] < indices[i + 1] and arr[pointers[i]] < min_value:
                min_value = arr[pointers[i]]
                min_index = i

        if min_index == -1:
            break

        temp.append(arr[pointers[min_index]])
        pointers[min_index] += 1

    arr[indices[0]:indices[-1]] = temp


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    k = 3
    k_way_merge_sort(arr, 0, len(arr) - 1, k)
    print("Sorted array:", arr)
