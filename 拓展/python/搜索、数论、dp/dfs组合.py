print("输入想要组合的")

a=list(input().split())

n=len(a)

vis=[0]*100

def shuchu():
    for i in range(n):
        if vis[i]:      #如果选a[i]
            print(a[i],end='')
    print(' ',end=' ')
    return

def dfs(step):
    if step==n:
        shuchu()
        return #记得终结
    else:
        vis[step]=0;dfs(step+1)#不选
        vis[step]=1;dfs(step+1)#选

        vis[step]=0 #别忘记恢复vis现场

dfs(0)
