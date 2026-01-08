from math import gcd

n=int(input())
a=list(map(int,input().split()))

l=0
r=n-1

#print(gcd(1,3))

summ=0
def dfs(l,r):
    for i in range(l+1,r):
        if gcd(a[i],a[l])!=1:
            l=i+1
            break
    for i in range(r-1,l,-1):
        if gcd(a[i],a[r])!=0:
            r=i-1
            break
        
    
while l<=r:
    zl=[]
    zr=[]

    for i in range(l+1,r):
        if gcd(a[i],a[l])!=1:
            l=i+1
            break
    for i in range(r-1,l,-1):
        if gcd(a[i],a[r])!=0:
            r=i-1
            break
    print(l,r)
    if l==l:
        print(-1)
        break
    summ+=2

if summ!=0:
    print(summ+1)

    
