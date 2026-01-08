from math import sqrt

n, k = map(int, input().split())
x = list(map(int, input().split()))

vis = [0] * n  # 标记数组
sum2 = 0  # 累计素数结果数量


# 判断素数函数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# DFS 搜索
def dfs(step, m):
    global sum2
    if m == k:  # 如果已经选够 k 个数
        total = 0
        for i in range(n):
            if vis[i]:
                total += x[i]
        if is_prime(total):  # 如果和是素数
            sum2 += 1
        return

    if step == n:  # 到达数组末尾时结束递归
        return

    # 不选当前数
    vis[step] = 0
    dfs(step + 1, m)

    # 选当前数
    vis[step] = 1
    dfs(step + 1, m + 1)

    # 回溯
    vis[step] = 0


# 启动 DFS
dfs(0, 0)
print(sum2)
