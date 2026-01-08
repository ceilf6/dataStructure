n=int(input())

if n<=1:
    print(-1)
else:
    
    lis=[]
    for i in range(n,0,-1):
        lis.append(i)
    
    lis[-2]=lis[-1]

    for i in lis:
        print(i,end=' ')
