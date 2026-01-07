from collections import deque

def bi_bfs(sta,end,get_nei):
    if sta == end:
        return 0
    staq=deque([sta])
    endq=deque([end])
    vissta={sta:0}
    visend={end:0}
    while staq and endq:
        if len(staq)<=len(endq):
            for i in range(len(staq)):
                cur=staq.popleft()
                cursteps=vissta[cur]
                for nei in get_nei(cur):
                    if nei not in vissta:
                        vissta[nei]=cursteps+1
                        staq.append(nei)
                        if nei in visend:
                            return visend[nei]+vissta[nei]
        else:
            for i in range(len(endq)):
                cur=endq.popleft()
                cursteps=visend[cur]
                for nei in get_nei(cur):
                    if nei not in visend:
                        visend[nei]=cursteps+1
                        endq.append(nei)
                        if nei in vissta:
                            return visend[nei]+vissta[nei]
    return -1

def get_nei(pos):
    x,y=pos
    neis=[]
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<=m-1 and 0<=ny<=n-1 and ma[nx][ny]!=0:
            neis.append((nx,ny))

    return neis



n,m=map(int,input().split())

idx=0
idy=0
ma=[[0]*m for i in range(n)]
for i in range(n):
    ma[i]=list(map(int,input().split()))
    if 2 in ma[i]:
        idy=i
        idx=ma[i].index(2)

end=(idx,idy)

k=int(input())
t=[]
for i in range(k):
    t.append((map(int,input().split())))
l=[]
for i in range(k):
    l.append(bi_bfs(t[i],end,get_nei))
print(l)

