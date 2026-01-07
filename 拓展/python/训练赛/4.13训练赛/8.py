n,m,h=map(int,input().split())

ma=[[0]*m for i in range(n)]

for i in range(n):
    ma[i]=list(map(int,input().split()))


f=[[0]*m for i in range(n)]

for i in range(n):
    l=0
    cnt=0
    for j in range(m):
        if ma[i][j]<0:
            cnt+=1
        elif ma[i][j]>h:
            f[i][l:j]=[cnt]*len(f[i][l:j])
            cnt=0
            l=j+1
        if j==m-1:
            f[i][l:]=[cnt]*len(f[i][j:])

f2=[[0]*m for i in range(n)]

for i in range(m):
    upp=0
    cnt=0
    for j in range(n):
        if ma[j][i]<0:
            cnt+=1
        elif ma[j][i]>h:
            for z in range(l,j):
                f2[z][i]=cnt
            cnt=0
            l=j+1
        if j ==n-1:
            for z in range(l,n):
                f2[z][i]=cnt

print(f)
print(f2)

maxx=0
for j in range(m):
    for i in range(n):
        if f[i][j]+f2[i][j]>maxx:
            maxx=f[i][j]+f2[i][j]
            idx=j
            idy=i

print(maxx)
print(idx,idy)
