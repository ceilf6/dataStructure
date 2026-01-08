n=int(input("输入有几个数"))

a=[0]*100


vis=[0]*100#对应a下标的数的使用情况

b=[0]*100
m=0
def dfs(step):
    global m
    if step==n+1:
        #m+=1
        
        for i in range(1,n+1):      #更新完毕ans，也可以在函数外输出
            print("%5d"%b[i],end='')
        print()
        
        return
    
    for i in range(1,n+1):
        if vis[i]==0:
            b[step]=a[i]
            vis[i]=1
            dfs(step+1)
            vis[i]=0

for i in range(1,n+1):a[i]=i

dfs(1)  #从第一个排起


print('\n',m)
