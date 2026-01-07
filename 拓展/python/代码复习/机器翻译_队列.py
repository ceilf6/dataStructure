m,n=map(int,input().split())

s=list(map(int,input().split()))

from collections import deque

queue=deque()


ans=0
for i in s:
    if i not in queue:
        ans+=1
    else:
        continue
    queue.append(i)
    if len(queue)==m+1:
        queue.popleft()
    

print(ans)
