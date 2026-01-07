t=int(input())
for i in range(t):
    n,x=map(int,input().split())

    if n!=x:
        l1=[j for j in range(x)]
        l2=[j for j in range(x+1,n)]

        l3=l1+l2+[x]

        print(*l3)
    else:
        l=[j for j in range(n)]
        print(*l)
