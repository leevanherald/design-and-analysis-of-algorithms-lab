def is_good_permutation(arr):
    return all(arr[i] != i + 1 for i in range(len(arr)))


def generate_permutations(length, current=[], visited=None, result=None):
    if visited is None:
        visited = [False] * (length + 1)
    if result is None:
        result = []

    if len(current) == length:
        if is_good_permutation(current):
            result.append(current[:])
        return result

    for i in range(1, length + 1):
        if not visited[i]:
            visited[i] = True
            current.append(i)
            generate_permutations(length, current, visited, result)
            current.pop()
            visited[i] = False

    return result


if __name__ == "__main__":
    t = 4
    result = []

    for length in range(1, t + 1):
        generate_permutations(length, [], [False] * (length + 1), result)

    for perm in result:
        print(perm)
    print(len(result))
