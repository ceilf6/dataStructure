n, q = map(int, input().split())
a = list(map(int, input().split()))

def count_arithmetic_subarrays(l, r):
    """高效计算区间[l,r]内等差子数组的数量 O(n²)"""
    if l > r:
        return 0
    
    length = r - l + 1
    if length == 1:
        return 1
    if length == 2:
        return 3  # [l], [r], [l,r]
    
    count = 0
    
    # 对于每个起始位置
    for i in range(l, r + 1):
        # 单个元素
        count += 1
        
        # 长度为2或以上的等差数列
        if i < r:
            count += 1  # 长度为2的总是等差数列
            
            # 尝试扩展长度>=3的等差数列
            if i + 1 < r:
                diff = a[i + 1] - a[i]
                j = i + 2
                
                # 贪心扩展：一次性找到以i开头的最长等差数列
                while j <= r and a[j] - a[j - 1] == diff:
                    count += 1
                    j += 1
    
    return count

# 进一步优化：预计算相邻差值
def count_arithmetic_subarrays_fast(l, r):
    """超高效版本 O(n)"""
    if l > r:
        return 0
    
    length = r - l + 1
    count = length  # 所有单元素子数组
    
    if length < 2:
        return count
    
    # 添加所有长度为2的子数组
    count += length - 1
    
    if length < 3:
        return count
    
    # 计算长度>=3的等差数列
    i = l
    while i <= r - 2:
        if a[i + 1] - a[i] == a[i + 2] - a[i + 1]:
            # 找到等差数列的起点
            diff = a[i + 1] - a[i]
            j = i + 2
            
            # 扩展到最长
            while j < r and a[j + 1] - a[j] == diff:
                j += 1
            
            # 长度为len的等差数列包含len*(len-1)/2 - len + 1个长度>=3的子数组
            ari_len = j - i + 1
            if ari_len >= 3:
                # 长度为k的等差数列中，长度>=3的子数组数量
                additional = 0
                for k in range(3, ari_len + 1):
                    additional += ari_len - k + 1
                count += additional
            
            i = j  # 跳过已处理的部分
        else:
            i += 1
    
    return count

# 处理查询
for _ in range(q):
    l, r = map(int, input().split())
    result = count_arithmetic_subarrays_fast(l - 1, r - 1)
    print(result)
