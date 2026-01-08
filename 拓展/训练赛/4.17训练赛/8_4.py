n, k, s = map(int, input().split())

from collections import defaultdict

# 统计每个t分数的不达标和达标学生数量
non_pat = defaultdict(int)
pat = defaultdict(int)

for _ in range(n):
    t, p = map(int, input().split())
    if t >= 175:
        if p >= s:
            pat[t] += 1
        else:
            non_pat[t] += 1

# 按t升序排列所有分数
sorted_ts = sorted(set(non_pat.keys()).union(set(pat.keys())))
ans = 0

for _ in range(k):
    last_t = -1
    for t in sorted_ts:
        if t > last_t:
            # 先尝试选不达标的学生
            if non_pat.get(t, 0) > 0:
                ans += 1
                non_pat[t] -= 1
                last_t = t
                # 同一轮中，可以选所有达标的
                if pat.get(t, 0) > 0:
                    ans += pat[t]
                    pat[t] = 0
            else:
                # 没有不达标的，选一个达标的
                if pat.get(t, 0) > 0:
                    ans += 1
                    pat[t] -= 1
                    last_t = t
                    # 选剩下的达标的
                    if pat[t] > 0:
                        ans += pat[t]
                        pat[t] = 0
        elif t == last_t:
            # 选所有达标的
            cnt = pat.get(t, 0)
            if cnt > 0:
                ans += cnt
                pat[t] = 0

print(ans)
