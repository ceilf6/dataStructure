n=int(input())

import math
mod=999999999
from collections import deque
a=deque()
b=deque()
for i in range(1,n+1):
    if math.gcd(i,mod)!=1:
        b.append(i)
    else:
        a.append(i)
print(a,b)
if len(b)>=n/3:
    for i in range(1,n+1):
        if i%3==2:
            s=b.popleft()
            print(s,end=' ')
        else:
            s=a.popleft()
            print(s,end=' ')
        if a:
            while a:
                s=a.popleft()
                print(s,end=' ')
        elif b:
            while b:
                s=b.popleft()
                print(s,end=' ')
else:
    print("Baka!")
