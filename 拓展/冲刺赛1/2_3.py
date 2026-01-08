
'''
k=(0+n-1)*n/2

k2=(k+k-(n-3))*(n-2)/2

k3=(k2+k2-(n-2)*(n-2))*(n-1)/2

k4=(k3+k3-(n-1)*(n-2)*(n-1))*n/2

print(int(k4%998244353))
'''
import math
n=int(input())
k=[0]*(n+1)
k[0]=(0+n-1)*n//2
f=1
if n==0 or n==1:
    print(0)
elif n==2:
    print(1)
else:
    for i in range(1,n):
        f*=i
        k[i]=((k[i-1]+k[i-1]-f*i)*(1+i)//2)%998244353
    print(k[n-1])
