import sys
sys.setrecursionlimit(100000)

n=int(input())
p=[int(input()) for _ in range(n)]
t=[[] for _ in range(n+1)]
r=-1
for i in range(n):
    if p[i]==0:
        r=i+1
    else:
        t[p[i]].append(i+1)
for ch in t:
    ch.sort()

d=0
k=-1
ok=1
for i in range(1,n+1):
    c=len(t[i])
    if c:
        if k==-1:
            k=c
        elif k!=c:
            ok=0
    d=max(d,c)

pre=[]
def dfs(x):
    pre.append(x)
    for y in t[x]:dfs(y)
dfs(r)

print(f"{d} {'yes' if ok else 'no'}")
print(' '.join(map(str,pre)))
