def fact(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod


def calc_updates(arr):
    updates = 0
    max_val = -1
    for num in arr:
        if max_val < num:
            max_val = num
            updates += 1
    return updates


def generate_permutations(n, current=[], visited=None):
    global max_updates
    if visited is None:
        visited = [False] * (n + 1)

    if len(current) == n:
        max_updates += calc_updates(current)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            current.append(i)
            generate_permutations(n, current, visited)
            current.pop()
            visited[i] = False


if __name__ == "__main__":
    n = int(input())
    max_updates = 0
    generate_permutations(n)
    print("maxupdates=", max_updates)
    print("avg=", max_updates / fact(n))
