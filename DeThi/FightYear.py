import json

with open('flights.json') as f:
    a = json.load(f)
t = int(input())
for _ in range(t):
    s = input().split()
    if s[1] == 'min':
        min = 0
        for x in a['flights']:
            if min < int(x['passengers']):
                min = int(x['passengers'])
        print(min)
    elif s[1] == 'max':
        max = 0
        for x in a['flights']:
            if max < int(x['passengers']):
                max = int(x['passengers'])
        print(max)
    elif s[1] == 'sum':
        sum = 0
        for x in a['flights']:
            sum += int(x['passengers'])
        print(sum)
    else:
        sum = 0
        for x in a['flights']:
            sum += int(x['passengers'])
        print(sum / len(a['flights']))