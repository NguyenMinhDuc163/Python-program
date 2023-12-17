import csv

with open('iris.csv') as file:
    f = csv.reader(file)
    a = [x for x in f]

dis = {'sepal_length':0, 'sepal_width':1, 'petal_length':2, 'petal_width': 3}
t = int(input())
for _ in range(t):
    s = input().split()
    if s[0] in a: print('Invalid')
    else:
        if a[2] == 'avg':
            sum = 0
            for x in a[1:]:
                sum += a[dis[a[1]]]
            print(f'{sum / len(a):.2f}')
        else:
            sum = 0
            for x in a[1:]:
                sum += float(x[dis[s[1]]])
            print(sum)

