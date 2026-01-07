N,M=map(int,input().split())

T=int(input())

ma=[]

for _ in range(N):
    ma.append(list(map(int,input().split())))

av=[[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if ma[i][j]<=T:
            av[i][j]=1

# 四角？

l=-1
r=-1
s=-1
x=-1

# 从上面往下走
flag=0
for i in range(N):
    if flag:
        break
    for j in range(M):
        if av[i][j]:
            s=i
            flag=1
            break

# 从左边往右走
flag=0
for j in range(M):
    if flag:
        break
    for i in range(N):
        if av[i][j]:
            l=j
            flag=1
            break

# 从下面上走
flag=0
for i in range(N-1,-1,-1):
    if flag:
        break
    for j in range(M):
        if av[i][j]:
            x=i
            flag=1
            break

flag=0
for j in range(M-1,-1,-1):
    if flag:
        break
    for i in range(N):
        if av[i][j]:
            y=j
            flag=1
            break
print(av)
print(y-l+1)
print(x-s+1)
