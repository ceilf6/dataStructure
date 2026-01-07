n, q = map(int, input().split())
a = list(map(int, input().split()))

def count_arithmetic_subarrays_optimal(l, r):
    """最优解法：数学公式 O(n)"""
    if l > r:
        return 0
    
    length = r - l + 1
    if length == 1:
        return 1
    if length == 2:
        return 3
    
    # 基础计数：所有长度1和2的子数组
    count = length + (length - 1)
    
    # 找到所有极大等差子数组
    i = l
    while i <= r - 2:
        # 检查当前位置是否是等差数列的开始
        diff = a[i + 1] - a[i]
        j = i + 1
        
        # 扩展等差数列
        while j < r and a[j + 1] - a[j] == diff:
            j += 1
        
        # 计算这个等差数列贡献的子数组数量
        ari_len = j - i + 1
        if ari_len >= 3:
            # 长度为k的等差数列中，长度>=3的等差子数组数量公式：
            # C(k,3) + C(k,4) + ... + C(k,k) = sum(k-m+1 for m in range(3, k+1))
            for k in range(3, ari_len + 1):
                count += ari_len - k + 1
        
        i = j  # 移动到下一个可能的起点
    
    return count

# 处理查询
for _ in range(q):
    l, r = map(int, input().split())
    result = count_arithmetic_subarrays_optimal(l - 1, r - 1)
    print(result)
