

import math

def max_dist(p, points):
    return max(math.hypot(p[0] - x, p[1] - y) for x, y in points)

def min_max(points,x_min,x_max,y_min, y_max):
    step=0.1
    best=float('inf')
    while step > 1e-4:
        x = x_min
        while x <= x_max:
            y = y_min
            while y <= y_max:
                best = min(best, max_dist([x,y], points))
                y += step
            x+=step
        x_min+=step
        x_max-=step
        y_min+=step
        y_max-=step
        step/=2
    return best

def dfs(step):
    if step==n:
        if sum(vis)==3:
            ans=[]
            for i in range(len(vis)):
                if vis[i]==1:
                    ans.append(dian[i])
            result.append(ans)
        return
    vis[step]=1
    dfs(step+1)
    vis[step]=0
    dfs(step+1)


t=int(input())

for i in range(t):
    n=int(input())
    dian=[]
    maxx=0
    maxy=0
    for j in range(n):
        dian.append(list(map(int,input().split())))

    for j in dian:
        maxx=max(j[0],maxx)
        maxy=max(j[1],maxy)

    result=[]
    vis=[0]*n
    dfs(0)
    minn=float('inf')
    for j in result:
        minn=min(minn,(min_max(j,0,0,maxx,maxy)))
    print(minn)
    

