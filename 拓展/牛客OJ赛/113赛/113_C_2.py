q = int(input())
K = []
maxx = -1
minn = float('inf')
flag = 1

for _ in range(q):
    parts = list(map(int, input().split()))
    if not parts:  # 处理空行（理论上输入应保证有至少一个元素）
        flag = 0
        K.append([])
        continue
    n = parts[0]
    current = parts[1:]  # 删除第一个元素（n）
    K.append(current)
    if not current:  # 处理后的列表为空
        flag = 0
    else:
        current_max = max(current)
        current_min = min(current)
        maxx = max(maxx, current_max)
        minn = min(minn, current_min)

# 检查是否有有效数据
if flag and (maxx == -1 or minn == float('inf')):
    flag = 0

if flag:
    try:
        vis = [-1] * (maxx - minn + 1)
    except:
        flag = 0
    else:
        for i in range(q):
            current = K[i]
            if not current:
                flag = 0
                break
            if sorted(current) != current:
                flag = 0
                break
            for num in current:
                idx = num - minn
                if vis[idx] != -1:
                    flag = 0
                    break
                vis[idx] = num
            if not flag:
                break
        if flag and (-1 in vis):
            flag = 0

print('YES' if flag else 'NO')
