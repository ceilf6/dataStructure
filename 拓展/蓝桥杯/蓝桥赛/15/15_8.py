N=int(input())

X=list(map(int,input().split()))

F=list(map(int,input().split()))

#公用下标

maxx=0

for i in range(N):
    x=X.copy()

    f=F[i]
    if f!=-1:
        x[f]=0
    else:
        x[f]=x[f]
    
    for j in range(N):
        if F[j]==i:
            x[j]=0

    
    for z in range(N):
        if x[z]!=0:
            mu=x[i]^x[z]
            maxx=max(maxx,mu)

print(maxx)
