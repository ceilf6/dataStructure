a,b,c,d=map(int,input().split())

al=a%10

d2=1
for i in range(b%4):
    d2=(d2*al)%10

d3=(d2*c+d)%10


if d3%2==1:
    print('YES')

else:
    print('NO')
