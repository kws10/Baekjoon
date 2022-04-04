case = int(input()) # 케이스 수 입력 받고
list = [] # 수 넣을 리스트 선언

for i in range(case): # 케이스 수 만큼 반복문 돌림
    x = int(input()) # x 인풋 받고
    list.append(x) # 리스트에 어펜드

list.sort() # 리스트 솔팅

for i in list: # i가 리스트 돌면서
    print(i)


