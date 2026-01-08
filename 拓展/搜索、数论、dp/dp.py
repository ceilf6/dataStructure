n = int(input())
courses = []
maxx=0
for _ in range(n):
    a, b, c, t = map(int, input().split())
    total = a + b + c
    maxx=max(maxx,t)
    if total <= t:
        courses.append((total,t))

#二维
courses=sorted(courses,key=lambda x:x[1])
ans=0
dp=[[0]*(maxx+1) for i in range(n)]
for i in range(1,len(courses)):
    for j in range(courses[i][0],courses[i][1]+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-courses[i][0]]+1)
        ans=max(ans,dp[i][j])
print(ans)


#一维
courses=sorted(courses,key=lambda x:x[1])
dp=[0]*(maxx+1)
ans=0
for v,t in courses:
    for j in range(t,v-1,-1):
        dp[j]=max(dp[j],dp[j-v]+1)
        if dp[j]>ans:
            ans=dp[j]
print(ans)
