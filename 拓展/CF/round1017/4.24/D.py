from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()  # 对需求数组进行排序
    
    def check(k):
        # 对于每个可能的插入位置，检查是否能满足所有需求
        for insert_pos in range(n + 1):
            # 创建一个有序数组，包含k和其他元素
            sorted_vals = sorted(a[:insert_pos] + [k] + a[insert_pos:])
            count = 0  # 记录能满足多少个需求
            j = len(sorted_vals) - 1  # 从最大的值开始匹配
            
            # 从大到小遍历需求
            for i in range(m-1, -1, -1):
                while j >= 0 and sorted_vals[j] >= b[i]:
                    j -= 1
                    count += 1
                if count >= m:  # 如果已经找到足够的匹配
                    return True
                    
            if count >= m:
                return True
        return False
    
    # 先检查不需要新花的情况
    if check(0):
        print(0)
        continue
    
    # 二分查找最小的k值
    left = 1
    right = max(max(b), max(a)) if a else max(b)
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)