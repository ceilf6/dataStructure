n=int(input())

c=list(map(float,input().split()))

summ=0
from collections import defaultdict
cnt=defaultdict(int)
while 1:
    a,b=map(int,input().split())

    if a==0 or b==0:
        break
    cnt[a]+=b

    summ+=b*c[a-1]

for i in range(1,n+1):
    print(cnt[i])

print(f"{summ:.2f}")

