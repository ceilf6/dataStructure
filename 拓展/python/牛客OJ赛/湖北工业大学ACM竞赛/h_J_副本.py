n = int(input())
courses = []
maxx=0
for _ in range(n):
    a, b, c, t = map(int, input().split())
    total = a + b + c
    maxx=max(maxx,t)
    if total <= t:
        courses.append((total,t))
'''
courses=sorted(courses,key=lambda x:x[1])
dp=[[0]*(maxx+1) for i in range(n)]
for j in range(courses[0][0],courses[0][1]+1):
    dp[0][j]=1
    
ans=0
for i in range(1,len(courses)):
    for j in range(courses[i][0],courses[i][1]+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-courses[i][0]]+1)
        ans=max(ans,dp[i][j])
print(ans)
'''
'''
courses=sorted(courses,key=lambda x:x[1])
dp=[0]*(maxx+1)
ans=0
for i in range(n):
    for j in range(courses[i][1],courses[i][0]-1,-1):
        dp[j]=max(dp[j],dp[j-courses[i][0]]+1)
        if dp[j]>ans:
            ans=dp[j]
'''

courses=sorted(courses,key=lambda x:x[1])
dp=[0]*(maxx+1)
ans=0
for v,t in courses:
    for j in range(t,v-1,-1):
        dp[j]=max(dp[j],dp[j-v]+1)
        if dp[j]>ans:
            ans=dp[j]
print(ans)
