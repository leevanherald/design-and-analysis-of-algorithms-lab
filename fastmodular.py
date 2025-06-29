def fastmod(a, pow, n):
    if pow == 1:
        return a % n
    elif pow % 2 == 0:
        return (fastmod((a * a) % n, pow // 2, n) % n)
    else:
        return (a * (fastmod(a, pow - 1, n) % n) % n)


if __name__ == "__main__":
    a = int(input())
    pow = int(input())
    n = int(input())
    print(fastmod(a, pow, n))
