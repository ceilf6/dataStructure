'''
分组背包模版代码

V, n = map(int, input().split())
from collections import defaultdict
group = defaultdict(list)
for _ in range(n):
    a, b, c = map(int, input().split())
    group[c].append((a, b))

F = [0] * (V + 1)
for k in group:  # K是字典，用in遍历每个组的实际编号
    for j in range(V, -1, -1):
        for cost, val in group[k]:
            if j >= cost:
                F[j] = max(F[j], F[j - cost] + val)
print(F[V])
'''

while 1:
    n,m = map(int,input().split()) # n门课即有几组 ，m天数是容量
    if not n or not m:
        break
    w = [[] for i in range(n)]
    for i in range(n):
        w[i] = [0] + list(map(int,input().split())) # 耗费天数=0，即0:没得学分
    #print(w)
    F = [0]*(m+1)
    for k in range(n):
        for j in range(m, -1, -1):
            for c in range(len(w[k])):#索引即耗费天数
                if j >= c:
                    F[j]=max(F[j],F[j - c]+ w[k][c])
    print(F[-1])
        
