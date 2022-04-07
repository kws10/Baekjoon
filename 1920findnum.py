

list_a = []
list_b = []

a = int(input())
list_a = list(map(int,input().split()))

b = int(input())
list_b = list(map(int,input().split()))

for i in range(len(list_b)):
    if list_b[i] in list_a:
       print(1)
    else:
       print(0)
