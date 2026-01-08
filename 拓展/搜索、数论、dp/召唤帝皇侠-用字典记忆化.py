from math import *

n=int(input())

a=[]

for i in range(n):
    a.append(int(input()))

meme={}#用字典记忆化

def N(n):
    sum=0
    start=1
    for i in range(n,0,-1):
        if i in meme:
            sum+=meme[i]
            start=i+1
            break

    for i in range(start,n+1):
        k=i/floor(sqrt(i))#向下取整是floor “地板”
        if int(k)==k:
            sum+=i

    meme[n]=sum
    
    return sum

a.sort()

for i in range(n):
    print(N(a[i])%998244353)
