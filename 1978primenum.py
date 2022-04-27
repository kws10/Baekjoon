import sys

n = int(sys.stdin.readline())
p = map(int,sys.stdin.readline().split())
cnt = 0

def findprime(num):
    if num==1:
        return False

    for i in range(2,num):
        if num%i == 0:
           return False

    return True

for i in p:
    if findprime(i) == True:
       cnt += 1

print(cnt)

