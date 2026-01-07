N=int(input())

for i in range(N):
    n=int(input())

    b=list(map(int,input().split()))

    summ=0
    for j in range(len(b)-1):
        if  b[j+1]!=b[j]:
            summ+=1

    summ+=1

    print(summ)
