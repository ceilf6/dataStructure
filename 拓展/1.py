b,c,l,r=map(int,input().split())

def f(x):
    return x**2+b*x+c

import math

l=math.ceil(l)

if l%2:
    l+=1

summ=0

for i in range(l,r+1,2):
    summ+=f(i)

print(summ*2)
