t=int(input())
from collections import deque

for _ in range(t):
    n,m,k=map(int,input().split())

    l=[i for i in range(1,1+k)]
    q=deque(l)

    ma=[[0]*m for i in range(n)]

    for i in range(m):#第一行
        ma[0][i]=q[0]
        q.rotate(-1)

    for i in range(1,n):
        while q[0]==ma[i-1][0]:
            q.rotate(-1)
        ma[i][0]=q[0]
        q.rotate(-1)
        
        for j in range(1,m):
            while q[0]==ma[i-1][j] or q[0]==ma[i][j-1]:
                q.rotate(-1)
            ma[i][j]=q[0]
            q.rotate(-1)

    for i in ma:
        print(*i)

    
    
