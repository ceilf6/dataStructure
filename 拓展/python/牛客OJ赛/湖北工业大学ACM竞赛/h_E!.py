n = int(input())
lr = []
sum_l = 0
sum_r = 0
for _ in range(n):
    l, r = map(int, input().split())
    lr.append((l, r))
    sum_l += l
    sum_r += r

# 检查是否存在解
if sum_l > 0 or sum_r < 0:
    print("No")
else:
    # 需要调整的总量,假设开始时都是l
    delta = -sum_l
    res = []
    possible = True
    for l, r in lr:
        # 当前数最多能增加的量,min的话是怕加多了
        add = min(delta, r - l)
        res.append(l + add)
        delta -= add
        if delta == 0:
            break
    # 剩余的数保持左端点
    for l, r in lr[len(res):]:
        res.append(l)
    if delta != 0:
        print("No")
    else:
        print("Yes")
        print(' '.join(map(str, res)))
