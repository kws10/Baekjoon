# 이진 탐색으로 풀어야됨
# 이진 탐색은 정렬 되어있는 리스트에서 적용

import sys

list_n = []
find = []

def binary_search(arr,search,start,end): # (리스트 , 서치값, start , end)

    while start <= end:
          mid = start + end // 2

          if arr[mid] == search:
             return True
          elif arr[mid] < search:
             start = mid+1
          else:
             end = mid-1

    return False

n = int(input())

list_n = list(map(int, sys.stdin.readline().split()))

k = int(input())
find = list(map(int, sys.stdin.readline().split()))

list_n.sort()

for i in range(k):
    if binary_search(list_n,find[i],0,len(list_n)-1):
       print("1")
    else:
       print("0")