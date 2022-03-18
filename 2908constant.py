a,b = map(int, input().split())

num1a= a//100 # 100의 자리수 구하기
num1b= (a%100) // 10 # a의 100으로 나눈 나머지에서 10의 자리 구함
num1c= a%10 # 1의 자리 가져오기

num1 = num1c*100 + num1b*10 + num1a

num2a = b//100
num2b = (b%100) // 10
num2c = b%10

num2 = num2c*100 + num2b*10 + num2a

if num1>num2:
   print(num1)
else:
   print(num2)