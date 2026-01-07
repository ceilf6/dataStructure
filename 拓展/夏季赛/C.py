n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

#题目意思！！每次购买第i种，也就是同一种多次购买！！

'''
from functools import cache

@cache
def dfs(i,j,k):
    if i<0:
        return 0

    if k==0:
        return 0

    #key='{i},{j},{k}'

    #if j>a[i]:
    ans=dfs(i-1,j,k)

    if k>0:
        ans=max(ans,dfs(i-1,j-a[i],k-1)+b[i]-(k-1)*c[i])

    return ans

res=0
for l in range(1,n):
    res=max(res,dfs(n,m,l))

print(res)
'''

items = []

for i in range(n):
    k = 0
    while True:
        happy = b[i] - k * c[i]
        if happy <= 0:
            break
        items.append((a[i], happy))
        k += 1

# 完全背包
dp = [0] * (m + 1)

for price, value in items:
    for j in range(m, price - 1, -1):
        dp[j] = max(dp[j], dp[j - price] + value)

print(max(dp))
