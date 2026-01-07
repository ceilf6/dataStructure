T=int(input())

import math

for _ in range(T):
    n=int(input())
    flag=1

    a=list(map(int,input().split()))
    if a[0]!=1:
        print('NO')
        continue

    for i in range(2,n+1):
        k=math.floor(math.log(i,2))

        if a[i-1]<2**k or a[i-1]>=2**(k+1):
            print('NO')
            flag=0
            break
    if(flag):
        print('YES')
