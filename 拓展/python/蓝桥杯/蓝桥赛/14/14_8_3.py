import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
MOD = 998244353
num = 0

def dfs(step, summ, last):
    global num

    if step>=6:
        summ-=last[step-5]

    if summ>m:
        return

    if step==n:
        num=(num+1)%MOD
        return



    # 处理下一步的选择
    next_step = step + 1
    
    if next_step % 2 == 1:
        # 下一步是奇数位，选择奇数
        for i in range(1, 10, 2):
            new_last = last.copy()
            new_last.append(i)
            dfs(next_step, summ + i, new_last)
    else:
        for i in range(0, 10, 2):
            new_last = last.copy()
            new_last.append(i)#不会影响原来的数组
            dfs(next_step, summ + i, new_last)

# 初始处理：第一位必须是奇数
for i in range(1, 10, 2):
    dfs(1, i, [0, i])

print(num % MOD)
