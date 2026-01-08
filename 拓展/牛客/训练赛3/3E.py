n=int(input())
import math

mapp=[[0]*(n+1) for i in range(n+1)]

for i in range(1,1+n):
    for j in range(1,1+n):
        mapp[i][j]=math.gcd(i,j)


def printt(mapp):
    output='\n'.join(' '.join(map(str,x))for x in mapp)
    print(output)

printt(mapp)

'''
I=1
for i in range(n-1,-1,-1):
    if math.gcd(i,n)!=1:
        I=i
        #print(i)
        break

gcdd=math.gcd(i,n)
if i!=1:
    l2=2*(gcdd-1)+(n-I)

print(min(l2,2*(n-1)))
'''
minn=float('INF')
for i in range(n,-1,-1):
    J=1
    for j in range(i-1,-1,-1):
        if math.gcd(j,i)!=1:
            J=j
            break
    gcdd=math.gcd(J,i)
    minn=min(minn,2*(gcdd-1)+(i-J)+2*(n-i))

print(minn)
