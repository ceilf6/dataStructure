import datetime

n=int(input())

t=[[0]*2 for i in range(n)]

s=['']*n

for i in range(n):
    s[i]=list(input().split())

for i in range(n):
    dt1=datetime.datetime.strptime(s[i][0],"%H:%M:%S")
    dt2=datetime.datetime.strptime(s[i][1],"%H:%M:%S")
    t[i][0]=dt1.timestamp()
    t[i][1]=dt2.timestamp()

t=sorted(t,key=lambda x:x[1])
cnt=1
r=t[0][1]
for i in range(1,n):
    if t[i][0]>=r:
        cnt+=1
        r=t[i][1]

print(cnt)
