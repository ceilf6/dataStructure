n,m=map(int,input().split())
MOD=998244353
a=list(map(int,input().split()))
b=[1]*n

def exgcd(b,m):
    if m==0:
        return b,1,0
    gcd,x,y=exgcd(m,b%m)
    return gcd,y,x-(b//m)*y

def mov_inv(b,m):
    gcd,x,y=exgcd(b,m)
    if gcd!=1:
        return
    return x%m
    
for i in range(m):
    l,r,x=map(int,input().split())

    for j in range(l,r+1):
        a[j-1]=a[j-1]*(r-l+1)+(x-a[j-1])
        b[j-1]*=(r-l+1)

for i in range(n):
    print(a[i]*mov_inv(b[i],MOD)%MOD,end=' ')
