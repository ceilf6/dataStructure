from collections import deque,defaultdict

def bfs_from_end(end,get_nei):
    vis={end:0}
    q=deque([end])
    while q:
        cur=q.popleft()
        cursteps=vis[cur]
        for nei in get_nei(cur):
            if nei not in vis:
                vis[nei]=cursteps+1
                q.append(nei)
    return vis

def get_nei(pos):
    x,y=pos
    neis=[]
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and ma[nx][ny]!=0:
            neis.append((nx,ny))
    return neis

m,n=map(int,input().split())
ma=[]
end=None
for i in range(m):
    row=list(map(int,input().split()))
    ma.append(row)
    if 2 in row:
        end=(i,row.index(2))

k=int(input())
t=[]
for i in range(k):
    x,y=map(int,input().split())
    t.append((y-1,x-1))

# 一次 BFS 求所有点到大本营的最短距离
distmap=bfs_from_end(end,get_nei)

res=[]
for i in range(k):
    if t[i] in distmap:
        res.append((distmap[t[i]],i+1))

if not res:
    print("No winner.")
else:
    ans=defaultdict(list)
    for time,id in res:
        ans[time].append(id)

    keyans=sorted(ans.keys())
    for t in keyans:
        if len(ans[t])==1:
            print(f"{ans[t][0]} {t}")
            break
    else:
        print("No winner.")
