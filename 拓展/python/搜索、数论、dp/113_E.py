n=int(input())
import math
a=[0]+list(map(int,input().split()))

pre=[0]*(n+1)

for i in range(len(a),0,-1):
    for j in range(i-1,0,-1):
        if math.gcd(a[i],a[j])!=1:
            pre[i]=j
            break

dp=[0]*n
for i in range(len(a),0,-1):
    
