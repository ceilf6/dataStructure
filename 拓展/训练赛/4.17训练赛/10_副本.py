import sys
sys.setrecursionlimit(100000)
#PTA里面不拓栈会报错非零返回，拓栈了就会mle，死局，得用stack模拟递归

n=int(input())#病毒种类总数 0到n-1

#from collections import defaultdict

d={}
inn=[0]*n #记录被指向
for i in range(n):
    l=list(map(int,input().split()))

    d[i]=l[1:]
    for j in d[i]:
        if not inn[j]:
            inn[j]=1
    

maxl=0
ans=[]
def dfs(b):
    global maxl
    global ans
    
    flag=0
    for j in d[b[-1]]:
        if vis[j]!=1:
            flag=1
            
            b2=b.copy()
            b2.append(j)
            vis[j]=1
            dfs(b2)
            
            vis[j]=0
                      

    if not flag:#当前最长了
        if len(b)>maxl:
            maxl=len(b)
            ans=b.copy()

        elif len(b)==maxl:
            if b<ans:#字典序比较
                ans=b.copy()
                
        return
'''
for i in range(n):
    vis=[0]*n
    
    vis[i]=1
    dfs([i])
'''
for i in range(n):
    if not inn[i]:
        source=i
        break

vis=[0]*n
vis[source]=1
dfs([source])

print(len(ans))
print(*ans)



'''   用bfs的话不同队列间的vis会被污染
def gei_nei(

from collections import deque
def bfs(sta):
    q=deque([sta])
    vis=(sta)

    while q:
        cur=q.popleft()
        for nei in get_nei(cur):

for i in range(n):
    bfs(i)
'''
