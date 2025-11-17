import heapq

n=int(input())
heap=[]

for _ in range(n):
    s=list(map(int,input().split()))
    for i in s:
        if len(heap)<n:
            heapq.heappush(heap,i)
        elif i>heap[0]:
            heapq.heapreplace(heap,i)

print(heap[0])