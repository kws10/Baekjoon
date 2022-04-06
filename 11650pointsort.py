count = int(input())
list = []

for i in range(count):
    x, y = map(int, input().split())
    list.append((x,y))


list.sort(key= lambda x:(x[1],x[0])) # x 좌표로 정렬


for i in list:
    print(i[0],i[1])