import json
with open('flights.json') as f:
    a = json.load(f)

t = int(input())
for _ in range(t):
    s = input().split()
    for x in a['flights']:
        if x['year'] == s[0] and x['month'] == s[1]:
            print(x['passengers'])
            break
    else: print('Invalid')