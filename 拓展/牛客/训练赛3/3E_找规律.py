n=int(input())
import math

i=1
for i in range(n-1,-1,-1):
    if math.gcd(i,n)!=1:
        I=i
        print(i)
        break

gcdd=math.gcd(i,n)
if i!=1:
    l2=2*(gcdd-1)+(n-I)

print(min(l2,2*(n-1)))
    
