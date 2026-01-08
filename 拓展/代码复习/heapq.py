l=list(map(int,input().split()))

import  heapq

heapq.heapify(l)

x=int(input())

minn=heapq.heappushpop(l,x)

print(minn)
