import math
from collections import deque


def f(n,m):
    t=1
    if n==m:
        print('Yes')
        return

    q=deque([n])
    vis=set([n])  #vis！！vis 是一个 set，
    #而 append() 是 list 的方法，应该使用 add() 来添加元素到 set 中

    while q and t<100000:
        x=q.popleft()

        if x*2==m:
            print('Yes')
            return
        if x*2 not in vis:
            q.append(x*2)
            vis.add(x*2)

        xsqrt=math.floor(math.sqrt(x))

        if xsqrt==m:
            print('Yes')
            return
        if xsqrt not in vis:
            q.append(xsqrt)
            vis.add(xsqrt)
        t+=1

    print('No')
    return

N=int(input())
for i in range(N):
    n,m=map(int,input().split())

    f(n,m)
    
