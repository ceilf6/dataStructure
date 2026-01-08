import math

n,k=map(int,input().split())
a=list(map(int,input().split()))

vis=[0]*n

sum2=0

def ispr(n):
    if n<2:
        return 0
    if n in (2,3):
        return 1
    if n%2==0 or n%3==0:
        return 0
    for i in range(5,int(math.sqrt(n)+1),6):
        if n%i==0 or n%(i+2)==0:
            return 0
    return 1


def dfs(step,m):
    global sum2
    if m==k:#结算 
        summ=0
        for i in range(n):
            if vis[i]:summ+=a[i]
        print(summ)
        '''
         if ispr(summ):
            sum2+=1
            print(summ)
        '''
        return          #必须要return

    if step >= n:  # 边界条件，防止step超出n的索引范围
        return
    
    vis[step]=0
    dfs(step+1,m)
    vis[step]=1
    dfs(step+1,m+1)

    vis[step]=0         #别忘记恢复现场！！！！

dfs(0,0)


'''
print(sum2)
'''


#??

def dfs2(step, m):
    global sum2

    if step >= n:  
        if m == 0:  # 确保选到了 k 个数
            summ = 0
            for i in range(n):
                if vis[i]: summ += a[i]
            print(summ)
        return

    vis[step] = 0
    dfs2(step + 1, m)
    vis[step] = 1
    dfs2(step + 1, m - 1)

    vis[step] = 0

dfs2(0,k)
