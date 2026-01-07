from math import *

N=10000000
prime=[0]*(N+1)
vis=[True]*(N+1)

def sie(n):
    for i in range(n+1):vis[i]=True

    for i in range(2,int(sqrt(n))+1):
        if vis[i]:
            for j in range(i*i,n+1,i):
                vis[j]=False

    k=0
    for i in range(2,n+1):
        if vis[i]:
            k+=1
            prime[k]=i

    return k

print(sie(100))
