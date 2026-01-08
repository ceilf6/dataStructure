print("输入数的个数")
n=int(input())
a=list(range(1,n+1))

m=int(input("输入要排列数的个数"))

vis=[0]*100#对应a下标的数的使用情况

b=[0]*100

def dfs(step):
    if step==m+1:
        for i in range(1,m+1):      #更新完毕ans，也可以在函数外输出
            print("%5d"%b[i],end='')
        print()
        return
    for i in range(n):
        if vis[i]==0:
            b[step]=a[i]
            vis[i]=1
            dfs(step+1)
            vis[i]=0

dfs(1)  #从第一个排起

