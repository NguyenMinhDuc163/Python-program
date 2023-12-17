def khoangCach(v1, v2):
    ans = 0
    for i in range(len(v1)):
        ans += (v2[i] - v1[i]) ** 2
    return ans ** 0.5

def mul(v1, v2):
    ans = 0
    for i in range(len(v1)):
        ans += v1[i] * v2[i]
    return ans
t = int(input())
for _ in range(t):
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    print(f'{khoangCach(v1, v2):.2f} {mul(v1,v2):.0f}')