n = int(input())
l = list(map(int, input().split()))

# 建立所有可能子串的起点索引
window_map = dict()
max_k = 10000 + 1  # 题目中最长碎纸条长度上限
for k in range(1, max_k + 1):
    for i in range(n - k + 1):
        key = tuple(l[i:i+k])
        if key not in window_map:
            window_map[key] = i  # 只记录第一次出现的位置（因为唯一解）

m = int(input())
res = []

for idx in range(1, m + 1):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    h = tuple(tmp[1:])
    pos = window_map.get(h, -1)
    res.append((pos, idx))

res.sort()
print(" ".join(str(x[1]) for x in res))
