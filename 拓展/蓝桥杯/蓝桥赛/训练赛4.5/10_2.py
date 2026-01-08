MOD = 998244353
max_x = 10**5

# 预处理逆元数组和前缀平方和
inv = [0] * (max_x + 2)
inv[1] = 1
for i in range(2, max_x + 1):
    inv[i] = MOD - MOD // i * inv[MOD % i] % MOD

pre_sum = [0] * (max_x + 2)
for i in range(1, max_x + 1):
    pre_sum[i] = (pre_sum[i-1] + inv[i] * inv[i]) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c0 = a.count(0)
    x = sum(a[:c0]) if c0 else 0
    if x == 0:
        print(0)
    else:
        C = n * (n - 1) // 2 % MOD
        print(C * pre_sum[x] % MOD)
