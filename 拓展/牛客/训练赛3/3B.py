n=int(input())

a=list(map(int,input().split()))

if n==1:
    print('-1')
elif    n%2==0:
    print(n//2)
else:
    print(n//2+1)
