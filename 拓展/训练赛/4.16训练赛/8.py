def s(n):
    su=0
    while n:
        su+=(n%10)
        n//=10
    return su

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    
    sa=s(a)
    sb=s(b)
    
    flag=0
    if a%sb==0:
        print('A')
        flag=1
    elif b%sa==0:
        print('B')
        flag=1
    if not flag:
        if a>b:
            print('A')
        else:
            print('B')
