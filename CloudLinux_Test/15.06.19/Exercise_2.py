def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    print(d)
    for p in range(1, l//2 + 1):
        ok = True
        for i in range(l - p):
            if d[l-1-i] != d[l-1-i - p]:
                ok = False
                break
        if ok:
            return p
    return -1


if __name__ == "__main__":
    print(solution(21))