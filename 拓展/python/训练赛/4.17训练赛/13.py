n=int(input())

from collections import defaultdict

d=defaultdict(list)

for i in range(n):
    s=(list(input().split('.')))
    l=len(s)
    d[l].append(s)

#s=sorted(s,key=lambda x:x[1]) 本就是位多更后面
print(d)

ans=[d[1]]

from itertools import combinations
'''
vis=[0]*n
res=[]
def dfs(step,a):#zuhe
    if step==n:
        ans=[]
        for i in range(n):
            if vis[i]:
                ans.append(a[i])
        res.append(ans)
        return

    vis[step]=1
    dfs(step+1)
    vis[step]=0
    dfs(step+1)
'''

for i in d.keys():
    result=combinations(d[i],2)
    print(result)
    
    '''
    for j in range(i):
        if [:j]==d[i][
    '''
