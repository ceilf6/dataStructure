import math

def sie(L,R):
    if L>R:return[]
    limit=math.isqrt(R)
    sieve=[True]*(limit+1)
    sieve[0:2]=[False]*2
    for i in range(2,math.isqrt(limit)+1):
        if sieve[i]:sieve[i*i::i]=[False]*len(sieve[i*i::i])
    primes=[i for i,f in enumerate(sieve) if f]
    
    isp=[True]*(R-L+1)
    for x in (0,1):
        if L<=x<=R:isp[x-L]=False
    for p in primes:
        start=max(p*p,(L+p-1)//p*p)
        for m in range(start,R+1,p):isp[m-L]=False
    return [i+L for i,p in enumerate(isp) if p]

print(sie(1,100))
