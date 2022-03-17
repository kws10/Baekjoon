
hour,minute = map(int,input().split()) # 띄어쓰기 무시하고 입력받는다. 알아두자.


if minute-45<0: # 45를 뺏을때 0보다 작으면
    if hour-1<0: # 0시보다 적을때의 예외처리 23시밖에 될 경우의 수가 없다.
        print(23,60+(minute-45)) # 23시에서 60분에서 아까의 차를 더해준다
    else: # 0시가 아니라면
        print(hour-1,60+(minute-45)) # 1시간을 빼준뒤 60분에서 분차를 빼준다.

else: # 45를 뺏을때 0보다 작지 않으면
    print(hour,minute-45) # 시간을 그대로 두고 있는 분에서 45분만 뺀다.


