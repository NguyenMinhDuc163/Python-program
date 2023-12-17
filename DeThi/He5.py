def check(n):
    return n == 0 or n == 1 or n == 2 or n == 3 or n == 4

def solve(a):
    for x in a:
        if not check(x):
            return False
    return sum(a) == 5
n = int(input())
for _ in range(n):
    try:
        a = list(map(int, input()))
        print('YES' if solve(a) else 'NO')
    except: print('NO')

