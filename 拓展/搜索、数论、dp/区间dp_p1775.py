N=int(input())

m=list(map(int,input().split()))

s=[0]*1000
s[0]=m[0]
for i in range(1,N):
    s[i]=s[i-1]+m[i]        

dp=[[1000]*1000 for _ in range(1000)]
#dp[l][L] 表示长度为l左端点为L 的最优结果
#上面错了，应该是遍历区间长度，但是？

#边界状态
for i in range(N):
    dp[1][i]=m[i]#长度为1

for i in range(N):
    for j in range(i,N):
        dp[i][j]=min(dp[i][j],dp[i][j]+s[j]-s[j-1]-(s[i]-s[i-1])
                            #移动加最后一个，减前面那个

print(dp[N][N-1])
