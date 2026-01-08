n=int(input())

A=list(map(int,input().split()))

summ=0
from collections import deque
for i in range(n):
    queue=deque()
    queue.append(A[i])

    minn=A[i]
    maxx=A[i]

    step=i+1
    while queue:
        current=queue.popleft()

        maxx=max(current)
        minn=min(current)
        summ=(summ+maxx*minn)%MOD

        new=current.copy()
        new.append(A[step])
        queue.append(new)
