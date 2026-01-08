INF = float('inf')
 
n, m, k = map(int, input().split())
s = ' ' + input()  # 添加前导空格使其变为1-based索引
ma = [list(map(int, input().split())) for _ in range(m)]
 
def floyd(ma):
    d = [[ma[i][j] for j in range(m)] for i in range(m)]
    for k in range(m):
        for i in range(m):
            for j in range(m):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
 
d = floyd(ma)

#前缀和
su = [[0]*(n+1) for i in range(m)]  # 修改大小为n+1

for i in range(m):
    for j in range(1, n+1):  # 从1开始到n
        su[i][j] = su[i][j-1] + d[ord(s[j])-ord('a')][i]

f = [INF]*(n+1)  # 修改大小为n+1
f[0] = 0
mx = [0]*m
for i in range(k, n+1):
    for col in range(m):
        mx[col] = max(mx[col], su[col][i-k]-f[i-k])
    for col in range(m):
        f[i] = min(f[i], su[col][i]-mx[col])
print(f[n])