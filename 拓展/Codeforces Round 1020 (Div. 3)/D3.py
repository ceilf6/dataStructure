t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    def check(k):
        # 创建数组副本，这样可以在不改变原数组的情况下尝试各种位置
        temp = a.copy()
        
        # 对于每个可能的插入位置，尝试插入值k
        for insert_pos in range(n + 1):
            curr_a = temp[:insert_pos] + [k] + temp[insert_pos:]
            pos = 0  # 当前选择的花的位置
            bi = 0   # 当前需要满足的要求索引
            
            # 尝试从左到右匹配每个需求
            while bi < m and pos < len(curr_a):
                if curr_a[pos] >= b[bi]:
                    bi += 1
                pos += 1
                
            if bi == m:  # 如果所有需求都满足了
                return True
                
        return False
    
    # 先检查不需要新花的情况
    if check(0):
        print(0)
        continue
    
    # 二分查找最小的k值
    left = 1
    right = max(max(b), max(a))
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)
