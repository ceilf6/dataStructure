M,N=map(int,input().split())

groups = [[] for _ in range(1000)]

for i in range(N):
    a, b, c = map(int, input().split())
    groups[c].append((a, b))
dp = [0] * (M + 1)

for group in groups:
    if not group:
        continue
    # 临时保存当前组的状态
    new_dp = dp[:]
    for a, b in group:
        for j in range(M, a - 1, -1):
            new_dp[j] = max(new_dp[j], dp[j - a] + b)
    dp = new_dp

print(dp[M])
