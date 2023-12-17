import csv

data = []
with open("iris.csv") as f:
    f1 = csv.reader(f)
    data = [row for row in f1]

t = int(input())
while t > 0:
    inp = input().split()
    tong = []
    for x in data[1:]:
        if x[2] == inp[1] and x[4] == inp[0]:
            tong += [float(x[0])]
    if len(tong) == 0:
        kq = "Invalid"
    else:
        kq = format(sum(tong) / len(tong), ".4f")
    print(kq)
    t -= 1

