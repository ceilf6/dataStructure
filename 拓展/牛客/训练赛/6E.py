n=int(input())

for i in range(n):
    x,y=map(int,input().split())

    n=int(y/(x+1))*2
    summ=(x+1)*n/2

    if summ<y:
        if summ+1>=y:
            n+=1
        elif summ+1+x>=y:
            n+=2

    print(n)
