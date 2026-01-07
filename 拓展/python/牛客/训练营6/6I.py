T=int(input())

for i in range(T):
    n,m=map(int,input().split())

    p=list(map(int,input().split()))

    for j in range(m):
        l,r,c=map(int,input().split())
        
        f=p[c-1]
        p2=p.copy()

        p2=p2[:l-1]+sorted(p2[l-1:r])+p2[r:]

        fi=p2.index(f)

        print(fi+1)
        
