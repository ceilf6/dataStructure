MOD = 10**9 + 7

def digit_sum(x):
    digits = list(map(int, str(x)))
    n = len(digits)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(pos, tight, total):
        if pos == n:
            return total
        res = 0
        up = digits[pos] if tight else 9
        for d in range(0, up + 1):
            res = (res + dfs(pos + 1, tight and d == up, total + d)) % MOD
        return res

    return dfs(0, True, 0)

T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    ans = (digit_sum(R) - digit_sum(L - 1)) % MOD
    print(ans)
