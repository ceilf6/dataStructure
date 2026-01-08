a=int(input())
b=int(input())
m=int(input())

def exgcd(b,m):
    if m==0:
        return b,1,0
    gcd,x,y=exgcd(m,b%m)
    return gcd,y,x-(b//m)*y

def mod_inv(b,m):
    gcd,x,y=exgcd(b,m)
    if gcd!=1:
        return None
    return x%m

print(a*mod_inv(b,m)%m)
