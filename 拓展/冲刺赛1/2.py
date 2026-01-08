import sys
sys.setrecursionlimit(100000000)
n=int(input())

summ=0
def dfs(step):
    global summ
    if step==n+1:
        #print(b)
        for i in range(2,len(b)):
            for j in range(1,i):
                if b[j]<b[i]:
                    summ+=1
        return

    
    for i in range(1,n+1):
        if vis[i]==0:
            b[step]=a[i]
            vis[i]=1
            dfs(step+1)
            vis[i]=0


a=[0]*(n+1)
b=[0]*(n+1)
vis=[0]*(n+1)
for i in range(1,n+1):
    a[i]=i

dfs(1)

print(int(summ%998244353))
