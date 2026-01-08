import math
def sie(L,R):
    if L>R:
        return []
    limit=math.isqrt(R)
    sieve=[True]*limit
    sieve[0:2]=[False]*2
    for i in range(2,math.isqrt(limit)+1):
        sieve[i*i::i]=[False]*len(sieve[i*i::i])
    primes=[i for i,f in enumerate(sieve) if f]

    isq=[True]*(R-L+1)
    for x in (0,1):
        if L<=x<=R:isq[x-L]=False

    for p in primes:
        start=max(p*p,(L+p-1)//p*p)
        for m in range(start,R+1,p):
            isq[m-L]=False
    return [i+L for i,f in enumerate(isq) if f]

print(sie(100,1000))
