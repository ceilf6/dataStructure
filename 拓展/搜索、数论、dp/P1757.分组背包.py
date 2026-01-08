M,N=map(int,input().split())

cnt=[0]*1000
m=[[0]*1000 for _ in range(1000)]
v=[[0]*1000 for _ in range(1000)]

l=0
for i in range(N):
    a,b,c=map(int,input().split())

    cnt[c]+=1
    m[c][cnt[c]]=a
    v[c][cnt[c]]=b
    l=max(l,c)

dp=[[0]*1000 for i in range(1000)]

for i in range(1,l+1):  #输入从第一组开始
    for j in range(M+1):
        for k in range(1,cnt[i]+1):
            '''
            if m[i][k]>j:
                dp[i][j]=max(dp[i-1][j],dp[i][j])
            else:
            '''
            if m[i][k]<=j:
                dp[i][j]=max(dp[i][j],dp[i-1][j-m[i][k]]+v[i][k])

print(dp[l][M])
    
