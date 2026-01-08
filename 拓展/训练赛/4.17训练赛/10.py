import datetime

n=int(input())

s=[]
for i in range(n):
    s.append(list(input().split(' - ')))

s=sorted(s,key=lambda x:x[0])

s=[['','00:00:00']]+s+[['23:59:59','']]

#print(s)

ans=[]
for i in range(1,len(s)):
    if s[i-1][1]!=s[i][0]:
        ans.append([s[i-1][1],s[i][0]])

for i in range(len(ans)):
    print(f'{ans[i][0]} - {ans[i][1]}')
