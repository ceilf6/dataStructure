n = int(input())  # 病毒种类总数 0到n-1

d = {}            # 存图
in_deg = [0] * n  # 记录每个点的入度，用来找源头

for i in range(n):
    temp = list(map(int, input().split()))
    k = temp[0]
    d[i] = temp[1:]
    for j in d[i]:
        in_deg[j] += 1  # 记录谁被指向了

# 找源头（入度为 0 的点）
for i in range(n):
    if in_deg[i] == 0:
        source = i
        break

print(source)

maxl = 0
ans = []

def dfs(b):
    global maxl, ans
    
    flag = 0
    for j in d[b[-1]]:
        if vis[j] != 1:
            flag = 1
            b2 = b.copy()
            b2.append(j)
            vis[j] = 1
            dfs(b2)
            vis[j] = 0  # 回溯

    if not flag:  # 当前路径到头了
        if len(b) > maxl:
            maxl = len(b)
            ans = b.copy()
        elif len(b) == maxl:
            if b < ans:  # 字典序比较
                ans = b.copy()
        return

# 只从源头出发
vis = [0] * n
vis[source] = 1
dfs([source])

print(len(ans))
print(*ans)
