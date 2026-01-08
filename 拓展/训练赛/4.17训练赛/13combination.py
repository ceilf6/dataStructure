from collections import defaultdict
from itertools import combinations

n = int(input())
d = defaultdict(list)

# 分类存储：按层级（即点的数量+1）分类
for _ in range(n):
    s = input()
    level = len(s.split('.'))
    d[level].append(s)

# 打印每层的所有组合
for level in sorted(d.keys()):
    
    # 所有两两组合
    for a, b in combinations(same_level_items, 2):
        sa=list(a.split('.'))
        sb=list(b.split('.'))
        for i in range(level):
            if 
                
