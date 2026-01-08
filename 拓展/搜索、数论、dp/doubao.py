MOD = 1234567891


def R(n):
    return int(str(n)[::-1])


def A(n):
    if n == 0:
        return 0
    sorted_str = ''.join(sorted(str(n)))
    return int(sorted_str.lstrip('0')) if sorted_str.lstrip('0') else 0


S = 7
target = 10**18
# 用于存储已经出现过的 S 值及其对应的迭代次数
seen = {}
for k in range(target):
    if S in seen:
        # 找到循环节
        start = seen[S]
        cycle_length = k - start
        remaining = (target - start) % cycle_length
        for _ in range(remaining):
            S = (R(S) + A(S)) % MOD
        break
    seen[S] = k
    S = (R(S) + A(S)) % MOD

print(S)
    
