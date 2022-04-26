import sys

n = int(sys.stdin.readline())
a = []
b = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

b=sorted(a)

for j in b:
    print(j)

