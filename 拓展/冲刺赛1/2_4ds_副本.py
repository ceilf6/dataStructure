n = int(input())
mod = 998244353
inv2 = (mod + 1) // 2

if n == 0 or n == 1:
    print(0)
elif n == 2:
    print(1 % mod)
else:
    max_fact = n - 1
    fact = [1] * (max_fact + 1)
    for i in range(1, max_fact + 1):
        fact[i] = fact[i-1] * i % mod
    
    k = [0] * n
    k[0] = (n * (n - 1) // 2) % mod
    
    for i in range(1, n):
        prev = k[i-1]
        term1 = (2 * prev) % mod
        term2 = (fact[i] * i) % mod
        combined = (term1 - term2) % mod
        combined = combined * (i + 1) % mod
        k[i] = combined * inv2 % mod
    
    print(k[n-1] % mod)
