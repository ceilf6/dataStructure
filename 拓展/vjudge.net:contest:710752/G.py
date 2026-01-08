n,m=map(int,input().split())


#from collections import deque

l=list(map(int,input().split()))
'''
q=deque()
l=0
r=0
vis=[0]*m
ans=[]
for i in range(n):
    if sum(vis)==m:
        ans.append((l,r))
        q=deque()
        l=r=i

    cur=l[i]
    if not vis[cur]:
        q.append(cur)
        r+=1
        continue

    if vis[cur]:
'''
d={}
for i in range(n-m):
    vis=[0]*m
    j=i
    while j<n and not sum(vis)==m:
        vis[l[j]-1]=1
        j+=1
        
    if sum(vis)==m:
        ll=j-i
        if ll not in d:
            d[ll]=(i,j)

d=sorted(d.items(),key=lambda x:x[0])
print(d[0][1][0]+1,d[0][1][1])
