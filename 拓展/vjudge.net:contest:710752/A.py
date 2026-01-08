a,b,n=map(int,input().split())

ma=[]
from collections import deque
for i in range(a):
    ma.append(list(map(int,input().split())))

max_h=[]

for i in range(a):
    q_max=deque()
    row_max=[]
    for cur in range(b):
        while q_max and ma[i][cur]>ma[i][q_max[-1]]:
            q_max.pop()

        q_max.append(cur)
        while q_max[0]<=cur-n:
            q_max.popleft()
        if cur>=n-1:
            row_max.append(ma[i][q_max[0]])
    max_h.append(row_max)

rows=a-n+1
cols=b-n+1
max_z=[[0]*cols for i in range(rows)]

for j in range(cols):
    q=deque()
    for cur in range(a):
        while q and max_h[cur][j]>max_h[q[-1]][j]:
            q.pop()
        q.append(cur)
        while q[0]<=cur-n:
            q.popleft()
        if cur>=n-1:
            idx=cur-(n-1)
            max_z[idx][j]=max_h[q[0]][j]





min_h=[]

for i in range(a):
    q_min=deque()
    row=[]
    for cur in range(b):
        while q_min and ma[i][cur]<ma[i][q_min[-1]]:
            q_min.pop()
        q_min.append(cur)
        while q_min[0]<=cur-n:
            q_min.popleft()
        if cur>=n-1:
            row.append(ma[i][q_min[0]])
    min_h.append(row)
    

rows=a-n+1
cols=b-n+1



min_z=[[0]*cols for i in range(rows)]

for j in range(cols):
    q=deque()
    for cur in range(a):
        while q and min_h[cur][j]<min_h[q[-1]][j]:
            q.pop()
        q.append(cur)
        while q[0]<=cur-n:
            q.popleft()
        if cur>=n-1:
            idx=cur-(n-1)
            min_z[idx][j]=min_h[q[0]][j]
mi=float('inf')

for i in range(rows):
    for j in range(cols):
        now=max_z[i][j]-min_z[i][j]
        mi=min(now,mi)

print(mi)

