T=int(input())
import bisect

for i in range(T):
    n,m=map(int,input().split())

    p=list(map(int,input().split()))

    for j in range(m):
        l,r,c=map(int,input().split())
        
        f=p[c-1]
        
        sub=p[l-1:r]
        fi=bisect.bisect_left(sorted(sub),f)
        fi+=l-1



        print(fi+1)
        
