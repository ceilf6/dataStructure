t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # 找到所有已知位置的和
    target = None
    cnt_missing = 0  # 统计-1的数量
    
    # 先通过已知位置确定目标和
    for i in range(n):
        if b[i] != -1:
            curr_sum = a[i] + b[i]
            if target is None:
                target = curr_sum
            elif target != curr_sum:
                print(0)
                break
        else:
            cnt_missing += 1
    else:  # 没有break才会执行
        if target is None:  # b全是-1的情况
            # 优化：直接计算可行解的范围
            max_a = max(a)
            min_a = min(a)
            # 对于任意i,j: ai + bi = aj + bj
            # 即 bi - bj = aj - ai
            # bi和bj都要在[0,k]范围内
            # 因此最大差值max_diff = max_a - min_a
            # x - ai 需要在[0,k]范围内，其中x是target
            # 所以 ai <= x <= ai + k
            # 对所有i都成立，则有：max_a <= x <= min_a + k
            
            if max_a > min_a + k:  # 差值太大，无解
                print(0)
            else:
                # x的范围是[max_a, min_a + k]
                # 只要x在这个范围内，就能保证所有bi都在[0,k]范围内
                ans = min_a + k - max_a + 1
                print(max(0, ans))
        else:
            # 已知target，检查所有-1位置填入的值是否在范围内
            valid = True
            for i in range(n):
                if b[i] == -1:
                    bi = target - a[i]
                    if bi < 0 or bi > k:
                        valid = False
                        break
            print(1 if valid else 0)
