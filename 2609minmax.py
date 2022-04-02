a, b = map(int,input().split())

min = 0
max = 0

mul=1
div=1

while True:
    if a%div == 0 and b%div == 0: # 둘다 나눠지면
       if (a==div) or (b==div): # div가 두수와 같아지는 타이밍에
           break # 반복문탈출
       else: # 그렇지 않으면
           max=div # 최대공약수에 div값 대입
           div = div + 1
    else: # 나눠지지 않으면
        div = div + 1 # 나누는값 +1

print(max) # max값 출력




