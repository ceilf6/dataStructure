n,m=map(int,input().split())
d=[[]for _ in range(m+1)]

for i in range(1,n+1):
    tmp=list(map(int,input().split()))[1:]
    for x in tmp:
        d[x].append(i)

q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    la,lb=len(d[a]),len(d[b])
    if la>lb:
        a,b=b,a
    s=set(d[b])
    cnt=0
    for x in d[a]:
        if x in s:
            cnt+=1
    print(cnt)
