n,m=map(int,input().split())
import math
k=math.ceil(m/n)
ans=[]
for i in range(n):
    a,b,c=map(int,input().split())
    for j in range(1,k+1):
        ans.append(a*j**2+b*j+c)

ans.sort()
print(*ans[:m])
