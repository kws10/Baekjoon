case = int(input())
list = []

for i in range(case):
   age, name = map(str,input().split())
   age = int(age)
   list.append((age,name))

list.sort(key = lambda x:x[0]) # (age, name) 에서 age로만 정렬

for i in list:
   print(i[0],i[1])



