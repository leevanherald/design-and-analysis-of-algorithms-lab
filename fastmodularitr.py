def fastmod(a, pow, n):
    ans = a
    for i in range(pow - 1):
        ans = (ans * a) % n
    return ans


if __name__ == "__main__":
    a = int(input())
    pow = int(input())
    n = int(input())
    print(fastmod(a, pow, n))
