n, k, s = map(int, input().split())

st = []
for _ in range(n):
    t_score, p_score = map(int, input().split())
    if t_score >= 175:
        st.append([t_score, p_score])

# 按天梯赛分数升序，再按PAT分数升序排序
st.sort(key=lambda x: (x[0], x[1]))

used = [False] * len(st)
ans = 0

for _ in range(k):
    last_score = -1
    for i in range(len(st)):
        if used[i]:
            continue
        t, p = st[i]
        if t > last_score:
            used[i] = True
            last_score = t
            ans += 1
        elif t == last_score and p >= s:
            used[i] = True
            ans += 1

print(ans)
