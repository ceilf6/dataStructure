from collections import *
s1 = input()
s2 = input()
pq1 = deque()
pq2 = deque()
find1 = dict()
find2 = dict()
pq1.append((s1, 0))
pq2.append((s2, 0))
find1[s1] = 0
find2[s2] = 0
ix, iy = [0, 1, 0, -1], [1, 0, -1, 0]
def solve1():
    s, step = pq1.popleft()
    s = list(s)
    idx = -1
    for i, x in enumerate(s):
        if x == '.':
            idx = i
            break
    x = idx // 3
    y = idx % 3
    for d in range(4):
        xx = x + ix[d]
        yy = y + iy[d]
        if xx >= 0 and xx < 3 and yy >= 0 and yy < 3:
            s[3 * x + y], s[3 * xx + yy] = s[3 * xx + yy], s[3 * x + y]
            p = ''.join(s)
            if p in find2:
                return step + find2[p] + 1
            if p in find1:
                s[3 * x + y], s[3 * xx + yy] = s[3 * xx + yy], s[3 * x + y]
                continue
            pq1.append((p, step + 1))
            find1[p] = step + 1
            s[3 * x + y], s[3 * xx + yy] = s[3 * xx + yy], s[3 * x + y]
    return -1
def solve2():
    s, step = pq2.popleft()
    s = list(s)
    idx = -1
    for i, x in enumerate(s):
        if x == '.':
            idx = i
            break
    x, y = idx // 3, idx % 3
    for d in range(4):
        xx = x + ix[d]
        yy = y + iy[d]
        if xx >= 0 and xx < 3 and yy >= 0 and yy < 3:
            s[3 * x + y], s[3 * xx + yy] = s[3 * xx + yy], s[3 * x + y]
            p = ''.join(s)
            if p in find1:
                return step + 1 + find1[p]
            if p in find2:
                s[3 * x + y], s[3 * xx + yy] = s[3 * xx + yy], s[3 * x + y]
                continue
            pq2.append((p, step + 1))
            find2[p] = step + 1
            s[3 * x + y], s[3 * xx + yy] = s[3 * xx + yy], s[3 * x + y]
    return -1
flag = False
while pq1 and pq2:
    t = -1
    if len(pq1) <= len(pq2):
        t = solve1()
    else:
        t = solve2()
    if t != -1:
        print(t)
        flag = True
        break
if not flag:
    print(-1)
