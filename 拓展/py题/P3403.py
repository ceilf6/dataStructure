from collections import deque

mx=int(input())
x,y,z=map(int,input().split())

def bfs():

    ans=1
    q=deque([1])
    vis=set([1])

    while q:
        cur=q.popleft()

        a1=cur+x
        a2=cur+y
        a3=cur+z

        if a1 not  in vis:
            if a1<=mx:
                vis.add(a1)
                q.append(a1)
                ans+=1


        if a2 not  in vis:
            if a2<=mx:
                vis.add(a2)
                q.append(a2)
                ans+=1

        if a3<=mx:
            if a3 not in vis:
                vis.add(a3)
                q.append(a3)
                ans+=1

    return ans

print(bfs())
