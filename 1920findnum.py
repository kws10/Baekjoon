# 이진 탐색으로 풀어야됨
# 이진 탐색은 정렬 되어있는 리스트에서 적용

def binary_search(a,search): # (리스트 , 서치값 )
    start = 0
    end = len(a) - 1

    mid = (start + end) // 2

    if mid == search:
       return mid
    elif mid < search:
       start = mid
    elif mid > search:
       end = mid

    









