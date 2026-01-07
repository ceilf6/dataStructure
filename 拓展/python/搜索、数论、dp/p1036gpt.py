import math

def ispr(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def dfs(step, m, current_sum):
    """深度优先搜索"""
    if m == k:
        if ispr(current_sum):
            print(current_sum)
            return 1
        return 0
    if step == n:
        return 0
    # 不选当前元素
    without_current = dfs(step + 1, m, current_sum)
    # 选当前元素
    with_current = dfs(step + 1, m + 1, current_sum + a[step])
    return without_current + with_current

# 输入处理
p = list(map(int, input().split()))
n, k = p[0], p[1]

print(f"数组长度：{n}, 选取个数：{k}")

a = list(map(int, input().split()))

if k > n or k < 0:
    print("选取个数不合法")
else:
    total_count = dfs(0, 0, 0)
    print(f"总共有 {total_count} 种方案")
