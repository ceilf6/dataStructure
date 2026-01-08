import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a  # 让索引从1开始
    max_size = n + 2
    pre = [0] * (n + 2)
    nxt = [float('inf')] * (n + 2)
    dp = [-1] * (n + 2)
    dp[0] = 0
    
    # 预处理pre和nxt数组
    for i in range(1, n + 1):
        for j in range(1, i):
            if math.gcd(a[i], a[j]) != 1:
                nxt[j] = min(nxt[j], i)
                pre[i] = max(pre[i], j)
    
    # 动态规划处理
    for i in range(1, n + 1):
        mn = 10**9
        for j in range(i, 0, -1):
            if nxt[j] > i:
                mn = min(mn, pre[j])
            else:
                if mn >= j and dp[j - 1] != -1:
                    dp[i] = max(dp[i], dp[j - 1] + 1)
    
    print(dp[n])

solve()
