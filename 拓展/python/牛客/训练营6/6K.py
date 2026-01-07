N=int(input())

for i in range(N):
    x,y=map(int,input().split())

    if y==1:
        if x%2==0:
            print('YES')
        else:
            print('NO')

    elif y%2==0:
        print('NO')

    elif (y-2*x-1)%4==0:
        print('YES')

    else:
        print('NO')
