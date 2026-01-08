MOD = 998244353

m = int(input())
A = list(map(int, input().split()))
A.sort()

if m == 0:
    print(0)
    exit()

max_n = m

# 预处理2的幂和逆元
pow2 = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    pow2[i] = (pow2[i-1] * 2) % MOD

inv_2 = pow(2, MOD - 2, MOD)
inv_pow2 = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    inv_pow2[i] = (inv_pow2[i-1] * inv_2) % MOD

# 计算前缀和数组pre_sum
pre_sum = [0] * m
pre_sum[0] = A[0] * inv_pow2[0] % MOD
for i in range(1, m):
    pre_sum[i] = (pre_sum[i-1] + A[i] * inv_pow2[i]) % MOD

result = 0
for i in range(m):
    a_i = A[i]
    if i == 0:
        term = a_i * a_i % MOD
    else:
        sum_prev = pow2[i-1] * pre_sum[i-1] % MOD
        term = a_i * (a_i + sum_prev) % MOD
    result = (result + term) % MOD

print(result)
