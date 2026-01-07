from math import *
import sys
sys.setrecursionlimit(10000)

n,k=map(int,input().split())

x=list(map(int,input().split()))

vis=[0]*n

sum2=0

def ispr(n):
    if n<2:
        return 0
    if n in (2,3):
        return 1
    if n%2==0 or n%3==0:
        return 0
    for i in range(5,int(sqrt(n)+1),6):
        if n%i==0 or n%(i+2)==0:
            return 0
    return 1


def dfs(step,m):
    global sum2
    if m==k:
        sum=0
        for i in range(n):
            if vis[i]:
                sum+=x[i]
        if ispr(sum): #注意层级
            sum2+=1
        return
    
    elif step==n:
        return
    vis[step]=0
    dfs(step+1,m)
    vis[step]=1
    dfs(step+1,m+1)

    vis[step]=0

dfs(0,0)  #别忘记启动dfs
print(sum2)
