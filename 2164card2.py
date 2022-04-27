import sys
from collections import deque

cnt = int(sys.stdin.readline())

card = deque()

for i in range(cnt):
    card.append(i+1)

while len(card)>1:
      card.popleft()
      card.append(card.popleft())

print(card[0])
