n,m=map(int,input().split())
 
'''#节点cost，注意：起点和终点得设为0. ------------
c=list(map(int,input().split()))
 
c[0]=0
c[n-1]=0
'''#------------------------------------------

edges=[]

for i in range(m):
    u,v,w=map(int,input().split())
    edges.append((u,v,-w))
    '''
    #别忘记双向边
    edges.append((v,u,w))
    '''

def bellman(n,edges,sta):
    INF=float('inf')
    d=[INF]*(n+1)           #注意输入起始从1开始，所以得n+1 ,初始化无边
    d[sta]=0                #d数组是从sta到各点的最短路径，自己到自己为0
 
 
    #n-1轮松弛
    for i in range(n-1):
        for u,v,w in edges:
            if d[u]!=INF:
                ncost=d[u]+w
                if ncost<d[v]:
            #从sta有边到u ，而且新路径更短
                    d[v]=ncost
 
 
    #第n轮:检测负环
    for u,v,w in edges:
        if d[u]!=INF and d[u]+w<d[v]:
            #print('Forever love')
            return None
 
    return d

d1=bellman(n,edges,1) #靠近是相互的:可以起始从1开始
d2=bellman(n,edges,n)           #也可以从n到1

if d1 and d2:
    if d1[n]<d2[1]:
        print(d1[n])
    else:
        print(d2[1])
else:
    print('Forever love')
'''
elif d1:
    print(d1[n])
elif d2:
    print(d2[1])
'''
