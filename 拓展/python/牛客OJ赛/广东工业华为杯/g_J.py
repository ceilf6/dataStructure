T=int(input())

import bisect as bi
for i in range(T):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))

    a.sort(reverse=0)

    
    idx=bi.bisect_left(a,m)

    ans=n-idx
    
    del a[idx:]

    
    maxx=m-a[-1]
    del a[-1]

    #print(a)
    i=len(a)-1

    #print(i)

    while i>-1:
        xu=maxx-a[i]

        while xu>=0:
            xu-=a[0]
            del a[0]
        ans+=1

        if a:
            del a[-1]

        i=len(a)-1

    print(ans+1)
