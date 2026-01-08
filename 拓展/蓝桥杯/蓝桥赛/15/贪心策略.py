b=list(map(int,input().split()))

def min_operations(nums):
    n = len(nums)
    d = nums.copy()
    operations = 0
    for i in range(n):
        while d[i] != 0:
            if i + 1 < n and d[i] * d[i + 1] > 0:
                # 符号相同，可以双操作
                k = min(abs(d[i]), abs(d[i + 1]))
                operations += k
                if d[i] > 0:
                    d[i] -= k
                    d[i + 1] -= k
                else:
                    d[i] += k
                    d[i + 1] += k
            else:
                # 单独处理当前元素
                operations += abs(d[i])
                d[i] = 0
    return operations


print(min_operations(b))
