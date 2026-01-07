n=int(input())

a=list(map(int,input().split()))

b=list(map(int,input().split()))

a2=a.copy()
a2.sort()
b2=b.copy()
b2.sort()


d={}
for i in range(n):
    d[a2[i]]=b2[i]

print(d)

ans=n
for i in range(n):
    if d[a[i]]==b[i]:
        ans-=1
import math
print(math.ceil(ans/2))
