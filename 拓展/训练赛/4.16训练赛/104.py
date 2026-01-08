n, c = map(int, input().split())
name = [''] * n
num = [[i, 0] for i in range(n)]  # 存每个学校剩余人数

for i in range(n):
    name[i], nn = input().split()
    num[i][1] = int(nn)

le = [[i, [], 0] for i in range(n)]  # [学校id, 考场空位列表, 考场数]
contact = [0] * n  # 每个学校联系的监考人数

rooms = []  # 全局考场列表，每个考场：[容量c, 学校id]

while any(x[1] > 0 for x in num):
    num = sorted(num, key=lambda x: x[1], reverse=True)
    sid, cnt = num[0]  # 当前人数最多的学校
    if cnt >= c:
        # 新开考场
        le[sid][1].append(c - c)  # 空位为0
        le[sid][2] += 1
        contact[sid] += 1
        rooms.append([sid, c - c])
        num[0][1] -= c
    else:
        # 先找已有赛场空位能放得下的
        found = False
        for rid in range(len(rooms)):
            r_sid, remain = rooms[rid]
            if r_sid != sid and remain >= cnt:
                continue  # 不同学校的就跳过
            if r_sid == sid and remain >= cnt:
                # 本校的已有赛场
                rooms[rid][1] -= cnt
                num[0][1] = 0
                found = True
                break
        if not found:
            # 新开一个考场
            le[sid][1].append(c - cnt)
            le[sid][2] += 1
            contact[sid] += 1
            rooms.append([sid, c - cnt])
            num[0][1] = 0

for i in range(n):
    print(name[i], contact[i])
print(len(rooms))
