
word = input().upper() # 모든 문자를 대문자로 바꾼다.
unique_word = list(set(word)) # 단어 중복되는 알파벳을 없애고 list로 만들어서 unique_word에 저장한다.

cnt_list = [] # 카운트할 리스트를 선언한다.

for x in unique_word: # unique_word 들을 검사하면서
    cnt = word.count(x) # word에서 unique_word에 있는 알파벳의 갯수를 cnt에 저장한다.
    cnt_list.append(cnt) # 리스트에 cnt에 걸린 알파벳을 저장

if cnt_list.count(max(cnt_list)) > 1: # cnt_list에서 최빈 값을 골라서 cnt_list에서 세보고 2개 이상이면
   print('?') # 물음표 출력
else: # 그렇지 않으면
   max_index = cnt_list.index(max(cnt_list)) # cnt리스트에서 최빈값이 몇번째에 있는지 max_index에 저장
   print(unique_word[max_index]) # unique_word에서 max_index 번째에 있는 값을 출력



