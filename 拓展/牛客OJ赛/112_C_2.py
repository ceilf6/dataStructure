import sys
sys.setrecursionlimit(10000)  # 提高递归深度限制

T = int(input())

n = [0] * T
m = [0] * T
k = [0] * T
q = [0] * T

for i in range(T):
    n[i], m[i], k[i], q[i] = map(int, input().split())

def dfs(step, summ, num, q,m):
    global flag
    
    if sum(num) == q:  # 如果找到符合条件的组合，直接返回
        flag = 1
        return

    if step == m:  # 递归终止条件
        return

    new_step = step + 1
    new_num = num.copy()

    for j in range(summ + 1):  # 遍历 0 到 summ
        new_num.append(j)
        new_summ = summ - j
        if new_summ >= 0:  # 确保新 summ 不会变负数
            dfs(new_step, new_summ, new_num, q,m)

for i in range(T):
    up = m[i] * (k[i] - 1)
    su = n[i] % k[i]
    suu = []

    while su <= k[i]:  # 计算所有可能的余数
        suu.append(su)
        su += k[i]

    flag = 0
    for j in suu:  # 遍历所有可能的 `summ`
        dfs(0, j, [], q[i],m[i])
        if flag:  # 一旦找到答案，就可以提前结束
            break

    if flag:
        print('YES')
    else:
        print('NO')
