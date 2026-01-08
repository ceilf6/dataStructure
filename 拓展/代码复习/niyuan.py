def exgcd(b,m):
    if m==0:
        return b,1,0
    gcd,x,y=exgcd(m,b%m)
    return gcd,y,x-(b//m)*y

def inv(b,m):
    gcd,x,y=exgcd(b,m)
    if gcd!=1:
        return
    return x%m

