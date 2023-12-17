def check(s):
    if len(s) != 8: return False
    idx = 0
    a = list(map(int, s))
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            idx = i - 1
            break
    for i in range(idx + 1, len(a)):
        if a[i] <= a[i - 1]: return False
    return True


t = int(input())
for _ in range(t):
    n = input()
    print('YES' if check(n) else 'NO')