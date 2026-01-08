def max_sum_after_k_operations(n, k, A):
    # 前缀和数组，prefix[i] 表示 A[0...i-1] 的和
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]
    
    # dp[i][j]表示经过i次操作，剩下j个元素的最大和
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 初始化动态规划表
    for i in range(k + 1):
        for j in range(n + 1):
            dp[i][j] = -float('inf')  # 初始设为负无穷
    
    # 填充动态规划表
    for i in range(k + 1):
        for j in range(n + 1):
            if i == 0:
                # 0次操作时，数组的和
                dp[i][j] = prefix[j] - prefix[0]
            elif j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + max(prefix[j] - prefix[0], prefix[j] - prefix[j-1]), dp[i][j])
            
    # 最终输出最大和
    return dp[k][n]

# 示例测试
n,k=map(int,input().split())

A=list(map(int,input().split()))
print(max_sum_after_k_operations(n, k, A))
