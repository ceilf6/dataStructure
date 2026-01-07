
n=int(input())

a=list(map(int,input().split()))

import math

su=0
MOD=998244353

for i in range(n):
    gc = a[i]
    su = (su + (i+1) * (i+1) % MOD * gc % MOD) % MOD
    
    for j in range(i+1, n):
        gc = math.gcd(gc, a[j])
        su = (su + (i+1) * (j+1) % MOD * gc % MOD) % MOD

print(su)
