import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    order = sys.stdin.readline().split()
    
    if order[0]=='1':
        queue.appendleft(order[1])
    elif order[0]=='2':
        queue.append(order[1])
    elif order[0]=='3':
        print(queue.popleft() if queue else -1)
    elif order[0]=='4':
        print(queue.pop() if queue else -1)    
    elif order[0]=='5':
        print(len(queue))
    elif order[0]=='6':
        print(0 if queue else 1)
    elif order[0]=='7':
        print(queue[0] if queue else -1)
    elif order[0]=='8':
        print(queue[-1] if queue else -1)   