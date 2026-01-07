n,m=map(int,input().split())

INF=float('inf')
ma=[[INF]*n for i in range(n)]
for i in range(n):
    ma[i][i]=0
for i in range(n-1):
    u,v=map(int,input().split())
    ma[u-1][v-1]=1
    ma[v-1][u-1]=1



def floyd(ma):

    d=[[ma[i][j] for j in range(n)]for i  in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

d=floyd(ma)

s=[]
for i in range(m):
    s.append(list(map(int,input().split())))

'''
for i in d:
    print(*i)
'''
for a,b,c in s:
    mn=float('inf')
    mni=-1
    for j in range(n):
        su=d[a-1][j]+d[b-1][j]+d[c-1][j]
        if su<mn:
            mni=j+1
            mn=su

    print(mni,mn)
