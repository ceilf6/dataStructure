import math

def isd(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return 0
    return 1

n,k=map(int,input().split())

l=list(map(int,input().split()))

from itertools import combinations

l2=list(combinations(l,k))

ans=0
for i in l2:
    if isd(sum(i)):
        ans+=1

print(ans)
