n=int(input())
l=list(map(int,input().split()))
import math
deep=math.log(n,2)

s=[1]
for i in range(1,int(deep)+1):
    s.append(s[-1]+2**i)


import bisect as bi
d=bi.bisect_left(s,n)


maxx=sum(l[:s[0]])
imax=1
for i in range(d):
    summ=sum(l[s[i]:s[i+1]])
    #print(summ)
    if summ>maxx:
        maxx=summ
        imax=i+2

print(imax)

