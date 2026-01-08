n, c = map(int, input().split())

name = [''] * n           # 学校名字
num = [[i, 0] for i in range(n)]  # [学校编号, 剩余人数]

for i in range(n):
    name[i], nn = input().split()
    num[i][1] = int(nn)

# le[i] 表示第 i 所学校的安排情况：[学校编号, 赛场集合, 目前还剩下的人数]
le = [[i, set(), num[i][1]] for i in range(n)]

arenas = []  # 每个赛场：[剩余空位, 当前已有的学校编号集合]

while any(x[2] > 0 for x in le):
    # 选出当前剩余人数最多的学校
    le = sorted(le, key=lambda x: x[2], reverse=True)
    for i in range(n):
        school_id, contact_set, remain = le[i]
        if remain == 0:
            continue
        if remain >= c:
            # 开一个新赛场
            arenas.append([c - c, {school_id}])
            le[i][2] -= c
            le[i][1].add(len(arenas) - 1)
        else:
            # 查找是否有空余 >= remain 的赛场
            flag = False
            for j in range(len(arenas)):
                space, school_set = arenas[j]
                if space >= remain:
                    arenas[j][0] -= remain
                    arenas[j][1].add(school_id)
                    le[i][1].add(j)
                    le[i][2] = 0
                    flag = True
                    break
            if not flag:
                # 开新赛场
                arenas.append([c - remain, {school_id}])
                le[i][1].add(len(arenas) - 1)
                le[i][2] = 0
        break  # 一轮只处理一个学校

# 输出
for i in range(n):
    print(f"{name[i]} {len(le[i][1])}")
print(len(arenas))
