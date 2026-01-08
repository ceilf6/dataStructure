from collections import deque

def bi_bfs(sta,end,get_nei):
    if sta==end:
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

res=[]
for i in range(k):
    dist=bi_bfs(t[i],end,get_nei)
    if dist!=-1:
        res.append((dist,i+1))

if not res:
    print("No winner.")
else:
    from collections import defaultdict
    ans=defaultdict(list)

    for i in range(len(res)):
        ans[res[i][0]].append(res[i][1])


    keyans=sorted(ans.keys())
    flag=0
    for i in range(len(keyans)):
        if len(ans[keyans[i]])<2:
            print(f"{ans[keyans[i]][0]} {keyans[i]}")
            flag=1
            break
    if not flag:
        print("No winner.")

