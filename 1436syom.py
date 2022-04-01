
number = int(input()) # 사용자에게 몇번째 영화인지 입력 받음
cnt = 0
six_num = 666 # 첫 666 들어가는 숫자

while True: # 무한 반복 돌림
    if '666' in str(six_num): # '666'이 six_num에 포함된다면 six_num 을 str로 변환
        cnt += 1 # 카운트 숫자 늘림
    if cnt == number: # 입력한 번째랑 cnt랑 같다면
       print(six_num) # 그 숫자를 출력함
       break # 끝냄.

    six_num += 1




