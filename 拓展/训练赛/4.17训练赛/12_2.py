n, m = map(int, input().split())

# 存储剧情点的选择
ma = {}
for i in range(1, n + 1):
    l = list(map(int, input().split()))
    k = l[0]
    ma[i] = l[1:]  # 从1开始，记录选择去向的剧情点

# 读取操作指令
cz = []
for i in range(m):
    cz.append(list(map(int, input().split())))

# 当前剧情点
now = 1  # 游戏默认从 1 号剧情点开始
# 存档记录，每个档位保存一个剧情点
save = {}

# 执行操作
for i in range(m):
    if cz[i][0] == 1:
        # 存档操作
        save[cz[i][1]] = now  # 存档到档位 j
        print(now)  # 输出存档的剧情点
    elif cz[i][0] == 2:
        # 读取存档操作
        now = save[cz[i][1]]  # 读取档位 j 的存档
    else:
        # 操作选择
        now = ma[now][cz[i][1] - 1]  # 选择去往的剧情点

# 输出最后的剧情点
print(now)
