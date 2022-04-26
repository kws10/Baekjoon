import sys

n = int(sys.stdin.readline())
a = []
c = []

def b(arr):
    i = 0
    while i >= len(arr):
        if arr[i]>arr[i+1]:
           arr[i] , arr[i+1] = arr[i+1] , arr[i]
        i= i+1

    return arr

for i in range(n):
    a.append(int(sys.stdin.readline()))

c = b(a)

for i in c:
    print(i)

