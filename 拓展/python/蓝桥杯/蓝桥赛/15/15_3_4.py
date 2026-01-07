from math import sqrt

n=int(input())

a=list(map(int,input().split()))

summ=n

for i in a:
    if i%2==1:
        summ-=1
    elif sqrt(8*i+1)%2==1:
        summ-=1

print(summ)
