a = 9
b = 16
n = 7
cnt = 0


def dfs(x, ra, rb):  # x第几个小朋友 ra a糖果还有几个 rb b糖果还有几个
    global cnt
    if ra < 0 or rb < 0:
        return
    if x > 7:
        if ra==0 and rb==0:
            cnt += 1
        return
    for i in range(2, 6):
        for j in range(i + 1):
            dfs(x + 1, ra - j, rb - i + j)


dfs(1, a, b)
print(cnt)
