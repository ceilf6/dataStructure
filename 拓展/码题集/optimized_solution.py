n, q = map(int, input().split())
a = list(map(int, input().split()))

def count_arithmetic_subarrays_optimized(l, r):
    """优化版本：O((r-l+1)²)"""
    count = 0
    
    # 枚举所有子区间的起点
    for i in range(l, r + 1):
        # 单个元素总是等差数列
        count += 1
        
        if i < r:
            # 两个元素总是等差数列
            count += 1
            
            # 尝试扩展更长的等差数列
            if i + 1 < r:
                diff = a[i + 1] - a[i]
                j = i + 2
                
                # 一直扩展到公差不匹配或超出范围
                while j <= r and a[j] - a[j - 1] == diff:
                    count += 1
                    j += 1
    
    return count

# 处理查询
for _ in range(q):
    l, r = map(int, input().split())
    result = count_arithmetic_subarrays_optimized(l - 1, r - 1)
    print(result)
