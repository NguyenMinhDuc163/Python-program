import json

f = open('flights.json')
b = json.load(f)

test = int(input())
for t in range(test):
    x = input().split()
    sum = 0
    for i in b['flights']:
        if int(i['year']) >= int(x[0]) and int(i['year']) < int(x[1]):
            sum += int(i['passengers'])

    print('Invalid' if sum == 0 else sum)