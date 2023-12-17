def check(s):
    ans = 1
    for i in range(len(s)):
        if (i + 1 ) % 2 == 1: ans *= int(s[i])
    return ans
t = int(input())
for _ in range(t):
    s = input()
    print(check(s.replace('0', '')))
