n=int(input())

temp=[]

#xmax=0;ymax=0
for i in range(n):
    te=list(map(int,input().split()))
    '''
    xmax=max(xmax,te[0])
    ymax=max(ymax,te[1])
    '''
    temp.append(te)

'''没必要建图
ma=[[0]*(ymax+1) for i in range(xmax+1)]

for i in range(n):
    ma[temp[i][0]][temp[i][1]]=temp[i][2]

for i in ma:
    print(*i)
'''

from collections import defaultdict
d=defaultdict(list)
for i in range(n):
    for j in range(n):
        if i!=j:
            x1,y1=temp[i][0],temp[i][1]
            x2,y2=temp[j][0],temp[j][1]
            if (x1-x2)**2+(y1-y2)**2<=temp[i][2]**2:
                d[i].append(j)
from collections import deque
def bfs(sta):
    q=deque([sta])
    l=1
    vis=[sta]
    while q:
        cur=q.popleft()
        for  nei in d[cur]:
            if nei not in vis:
                vis.append(nei)
                l+=1
                q.append(nei)
    return l

mx=0
for i in range(n):
    mx=max(mx,bfs(i))
print(mx)