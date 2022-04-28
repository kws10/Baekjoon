
import sys

snt = list(sys.stdin.readline().split())

def check(n):
    if(n.count('(') == n.count(')') and n.count('[') == n.count(']')):
       return True
    else:
       return False

while(snt != '.'):
    if check(snt)==True:
       print('yes')
    else:
       print('no')

    snt = list(sys.stdin.readline().split())



