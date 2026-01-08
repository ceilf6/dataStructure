n,m=map(int,input().split())

ma={}
for i in range(1,n+1):
    l=list(map(int,input().split()))
    k=l[0]
    ma[i]=l[1:]#从1开始?


save={}
now=1

for i in range(m):
    temp=list(map(int,input().split()))
    
    if temp[0]==1:
        save[temp[1]]=now
        

        print(now)
        
    elif temp[0]==2:
        now=save[temp[1]]
    else:
        now=ma[now][temp[1]-1]#第j个：从1开始？
        
print(now)
