case = int(input())
lise = []

for i in range(case):
   age, name = map(str,input().split())
   age = int(age)
   list.append((age,name))


list.sort(key = lambda x:x[0])

for i



