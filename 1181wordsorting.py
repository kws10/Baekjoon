cnt = int(input())
word_list=[]

for i in range(cnt):
    word_list.append(input())

word_list.sort()
word_list.sort(key=len)

for j in word_list:
    print(j)

