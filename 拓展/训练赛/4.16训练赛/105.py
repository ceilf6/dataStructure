n, c = map(int, input().split())
name = [''] * n
num = [[i, 0] for i in range(n)]
school_id = {}  # 学校缩写 -> 编号
for i in range(n):
    name[i], nn = input().split()
    num[i][1] = int(nn)
    school_id[name[i]] = i

le = [[i, [], 0] for i in range(n)]  # 每个学校：[编号, [空位列表], 总考场数]
monitor = [set() for _ in range(n)]  # 每个学校需联系的监考老师集合
rooms = []  # 所有考场 [空位, 负责学校id]，编号从 0 开始

while any(x[1] > 0 for x in num):
    num.sort(key=lambda x: x[1], reverse=True)
    sid, cnt = num[0]

    if cnt >= c:
        # 新开一个赛场
        rooms.append([c - c, sid])  # 空位为0，负责人是sid学校的老师
        le[sid][1].append(0)
        le[sid][2] += 1
        monitor[sid].add(len(rooms) - 1)
        num[0][1] -= c
    else:
        # 优先寻找空位足够的已有赛场（编号最小）
        found = False
        for rid in range(len(rooms)):
            free, owner = rooms[rid]
            if free >= cnt:
                # 填进去
                rooms[rid][0] -= cnt
                monitor[sid].add(rid)
                num[0][1] = 0
                found = True
                break
        if not found:
            # 新开赛场
            rooms.append([c - cnt, sid])  # 新赛场由 sid 学校负责
            le[sid][1].append(c - cnt)
            le[sid][2] += 1
            monitor[sid].add(len(rooms) - 1)
            num[0][1] = 0

# 输出
for i in range(n):
    print(f"{name[i]} {len(monitor[i])}")
print(len(rooms))
