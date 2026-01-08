import sys
sys.setrecursionlimit(10000000)

a=[2*i-2 for i in range(1,10000000)]


n=len(a)

vis=[0]*n
k=[]
'''
def dfs(step,m,M):

    if step >= n:#千万别忘记边界检查！！！  
        # 防止 step 超出 vis 数组长度
        return

    if m==M:#结算
        summ=0
        for i in range(n):
            if vis[i]:summ+=a[i]

        if summ not in k:
            
            k.append(summ)
        return

    vis[step]=0
    dfs(step+1,m,M)

    vis[step]=1
    dfs(step+1,m+1,M)

    vis[step]=0

for i in range(2,n):
    dfs(0,0,i)
k.sort()
'''
for i in range(2,n):
    for j in range(n-i):
        summ=sum(a[j:j+i])
        if summ not in k:
            k.append(summ)

k.sort()

N=int(input())
for i in range(N):
    ki=int(input())
    print(k[ki-1])
