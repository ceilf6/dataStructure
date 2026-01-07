a,b,m=map(int,input().split())

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

B=mov_inv(b,m)
print(a*B%m)
