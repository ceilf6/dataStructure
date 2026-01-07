
from collections import deque
n,m,a,b=map(int,input().split())

'''
A=[[]for i in range(n)]
for i in range(n):
    A[i]=list(map(int,input().split()))
'''
A=[list(map(int,input().split())) for i in range(n)]

maxx=[]
minn=[]

k=b
for i in range(n):
    q=deque()
    result=[]

    for current in range(len(A[0])):
        while q and A[i][current]>A[i][q[-1]]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:#超出了左边界
            q.popleft()

        if current>=k-1:#形成窗口后记录最大值
            result.append(A[i][q[0]])
    maxx.append(result)
    
minn=[]
for i in range(n):
    q2=deque()
    result2=[]
    for current in range(len(A[0])):
        while q2 and A[i][current]<A[i][q2[-1]]:
            q2.pop()
        q2.append(current)

        while q2[0]<=current-k:
            q2.popleft()

        if current>=k-1:
            result2.append(A[i][q2[0]])
    minn.append(result2)

k=a
maxx2=[[0]*(m-b+1)for i in range(n-a+1)]#记得预分配地址
minn2=[[0]*(m-b+1)for i in range(n-a+1)]

for j in range(m-b+1):
    q=deque()

    for current in range(n):
        while q and maxx[current][j]>maxx[q[-1]][j]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:
            q.popleft()

        if current >=k-1:
            maxx2[current-k+1][j]=maxx[q[0]][j]

    
for j in range(m-b+1):
    q=deque()
    for current in range(len(minn)):
        while q and minn[current][j]<minn[q[-1]][j]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:
            q.popleft()

        if current >=k-1:
            minn2[current-k+1][j]=minn[q[0]][j]
summ=0
for i in range(len(maxx2)):
    for j in range(len(minn2[0])):
        summ=(summ+maxx2[i][j]*minn2[i][j])#选的是max的...变量名！
                                            #应该是2的啊，而且没取mod

print(summ)

