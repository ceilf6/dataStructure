n,m=map(int,input().split())
d={}  # 物品 -> 拥有人编号集合

for i in range(1,n+1):
    tmp=list(map(int,input().split()))[1:]
    for x in tmp:
        if x not in d:
            d[x]=set()
        d[x].add(i)

q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    if a in d and b in d:
        print(len(d[a]&d[b]))
    else:
        print(0)
