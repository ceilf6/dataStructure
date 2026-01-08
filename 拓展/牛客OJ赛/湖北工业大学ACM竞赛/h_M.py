from collections import deque

def f_max(list,k):
    q=deque()
    result=[]

    for current in range(len(list)):
        while q and list[current]>=list[q[-1]]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:
            q.popleft()

        if current>=k-1:
            result.append(list[q[0]])
    return result

def f_min(list,k):
    q=deque()
    result=[]

    for current in range(len(list)):
        while q and list[current]<=list[q[-1]]:
            q.pop()
        q.append(current)

        while q[0]<=current-k:
            q.popleft()

        if current>=k-1:
            result.append(list[q[0]])
    return result

MOD=998244353
n=int(input())

A=list(map(int,input().split()))
summ=0

for i in range(n):
    for j in range(1,n-i+1):
        maxx=max(f_max(A[i:],j))
        minn=min(f_min(A[i:],j))
        summ=(summ+maxx*minn)%MOD
        
'''
maxx=[]
minn=[]
for j in range(1,n+1):
    maxx.append(f_max(A,j))
    minn.append(f_min(A,j))
for i in range(len(maxx)):
    for j in range(len(maxx[i])):
        summ=(summ+maxx[i][j]*minn[i][j])%MOD
'''
print(summ)
