n, q = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    # 预处理：对每个位置，计算以它结尾的最长等差数列长度
    dp = [1] * n  # dp[i] 表示以i结尾的最长等差数列长度
    
    for i in range(1, n):
        if i >= 2 and a[i] - a[i-1] == a[i-1] - a[i-2]:
            dp[i] = dp[i-1] + 1
        elif i >= 1:
            dp[i] = 2
    
    def count_fast(l, r):
        if l > r:
            return 0
        
        length = r - l + 1
        # 基础：所有长度1和2的子数组
        result = length
        if length > 1:
            result += length - 1
        
        # 计算长度>=3的等差子数组
        for i in range(l + 2, r + 1):
            # 以位置i结尾，在区间[l,r]内的等差子数组数量
            max_len = min(dp[i], i - l + 1)
            if max_len >= 3:
                result += max_len - 2
        
        return result
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(count_fast(l - 1, r - 1))

solve()
