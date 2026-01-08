n, m = map(int, input().split())

MOD = 998244353
num = 0

def dfs(step, summ, last):
    global num

    # 如果当前位数超过5位，需要减去最早的一位
    if step >= 6:
        summ -= last[step - 5]

    # 如果 5 位窗口的和超过 m，终止搜索
    if summ > m:
        return

    # 如果达到目标长度，计数+1
    if step == n + 1:
        num = (num + 1) % MOD
        return

    if step % 2 == 1:  # 奇数位放奇数
        for i in range(1, 10, 2):
            last.append(i)
            dfs(step + 1, summ + i, last)
            last.pop()  # 回溯
    else:  # 偶数位放偶数
        for i in range(2, 10, 2):
            last.append(i)
            dfs(step + 1, summ + i, last)
            last.pop()  # 回溯

# 初始时根据 n 的奇偶性决定第一个数
if n % 2 == 1:
    for i in range(1, 10, 2):  # 奇数位
        dfs(1, i, [0, i])
else:
    for i in range(2, 10, 2):  # 偶数位
        dfs(1, i, [0, i])

print(num)
