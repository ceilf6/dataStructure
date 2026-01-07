n,m=map(int,input().split())

ma={}
for i in range(1,n+1):
    l=list(map(int,input().split()))
    k=l[0]
    ma[i]=l[1:]#从1开始


cz=[]
for i in range(m):
    cz.append(list(map(int,input().split())))

print(ma)
print(cz)
save={}
now=1#默认1开始

for i in range(m):
    if cz[i][0]==1:
        save[cz[i][1]]=now
        

        print(now)
        
    elif cz[i][0]==2:
        now=save[cz[i][1]]
    else:
        now=ma[now][cz[i][1]-1]#第j个：从1开始？
        
print(now)
