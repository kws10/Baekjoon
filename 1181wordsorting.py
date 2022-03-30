cnt = int(input()) # 단어 개수 입력받고
word_list=[] # 단어리스트 선언하고

for i in range(cnt): #단어 개수 만큼 반복문 돌리고
    word_list.append(input()) # 리스트에 단어 입력받고

set_list = set(word_list) #리스트에 중복을 제거
word_list = list(set_list) #다시 리스트로 변환
word_list.sort() #글자를 사전순서로 정렬하고
word_list.sort(key=len) #글자순서로 정렬

for j in word_list: #워드리스트 돌면서
    print(j) # 출력

