ans = []
a, k, n = map(int, input().split())
for i in range(0, n + 1, k):
    if i > a: ans.append(str(i - a))
print(-1 if ans == [] else ' '.join(ans))