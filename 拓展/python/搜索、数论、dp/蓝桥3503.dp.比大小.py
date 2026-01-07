s=input()
dp=[[0]*5010 for _ in range(5010)]
ans=0
for k in range(2,len(s)):
    for i in range(len(s)-k):
        j=i+k
        if s[i]>s[j]:dp[i][j]=1
        if s[i]<s[j]:dp[i][j]=0
        if s[i]==s[j]:dp[i][j]=dp[i+1][j-1]
        if dp[i][j]:ans+=1
print(ans)
