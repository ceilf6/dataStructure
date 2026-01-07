T=int(input())

def bellman(n,edges,sta):
    INF=float('inf')
    d=[INF]*(n+1)
    d[sta]=0

    for i in range(n-1):
        for u,v,w in edges:
            ncost=d[u]+w
            if ncost<d[v]:
                d[v]=ncost
                
    for u,v,w in edges:
        ncost=d[u]+w
        if ncost<d[v]:
            return 1
        
    return 0#得第n轮所有边判断完才能下决定
    

for _ in range(T):
    n,m=map(int,input().split())

    edges=[]
    for i in range(m):
        u,v,w=map(int,input().split())
        if w>=0:
            edges.append((u,v,w))
            edges.append((v,u,w))
        else:
            edges.append((u,v,w))

    flag=bellman(n,edges,1)
    if flag:
        print('YES')
    else:
        print('NO')

    
