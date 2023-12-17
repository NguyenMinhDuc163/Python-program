import math


def snt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return n > 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = sum([int(x) for x in str(math.gcd(a, b))])
    print('YES' if snt(ans) else 'NO')