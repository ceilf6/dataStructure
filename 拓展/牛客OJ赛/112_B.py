import math

n=int(input())

a=list(map(int,input().split()))

hmax=-1

for i in range(1,n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        h=a[i]-math.floor((a[i-1]+a[i+1])/2)
        hmax=max(hmax,h)

print(hmax)
