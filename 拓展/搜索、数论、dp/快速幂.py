import math

print(pow(2,3,10))

def fastpow(a,n,m):
    ans=1
    while n:
        if n&1:ans*=a
        a=a**2%m
        n>>=1
    return ans%m

print(fastpow(2,3,100000))


print(math.pow(2.0,3))
