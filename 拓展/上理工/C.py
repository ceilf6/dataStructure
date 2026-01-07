T = int(input())

#import bisect
import math

for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    c=[]
    for i in range(n):
        if b[i]>=a[i]:
            c.append(b[i]-a[i])
        else:
            c.append(m+b[i]-a[i])

    c.sort()
    '''
    if c[-1]==0:
        print(0)
        continue
    '''
    #idx=bisect.bisect_left(c,math.ceil(m/2))

    '''
    if(m-c[0])<=c[0]:
        j=0

    else:
        j=1

        while(j<n):
            if (m-c[j])<=(c[j]-c[j-1]):
                break
            j+=1
    '''
    ans=m-c[0]

    #print(c,j,idx)
    for j in range(n):
        ans=min(ans,c[j-1]+m-c[j])

    ans=min(ans,c[-1])

    print(ans)
        
    #if j<n:
        #print(c[j-1]+m-c[j])
    
    #else:
    #    print(c[-1])

    #print()

