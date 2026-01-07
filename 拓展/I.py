n,m,x,ch=input().split()

n,m,x=int(n),int(m),int(x)

ma=[]

for i in range(n*x):
    ma.append(input())

#print(ma)

ans=[]

def find(i,j):
    for d1 in range(x):
        for d2 in range(x):
            if ma[i*x+d1][j*x+d2]==ch:
                return 1

    return 0

for i in range(n):
    res=[]
    for j in range(m):
        res.append(find(i,j))
    ans.append(res)

for i in ans:
    for j in i:
        print(j,end='')
    print()
    #print(*i)
