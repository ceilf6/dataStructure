t=int(input())

from collections import defaultdict
for i in range(t):
    n,m=map(int,input().split())

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    d=defaultdict(list)
    for j in range(n):
        for k in range(j,m):
            if a[j]>=b[k]:
                d[j].append(k)

    print(d)
                
