n=int(input())

a=list(map(int,input().split()))

dp=[0]*n

flag=1
for i in range(n-1,0,-1):
    if flag==1:
        dp[i-1]=dp[i]+(a[i]>a[i-1])*a[i]
    else:
        dp[i-1]=dp[i]+(a[i]<a[i-1])*a[i]
    flag=(flag+1)%2

print(dp)
