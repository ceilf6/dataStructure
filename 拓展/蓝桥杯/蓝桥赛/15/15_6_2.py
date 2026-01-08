import math

def ispr(n):
    if n<2:
        return 0
    if n in (2,3):
        return 1
    if n%2==0 or n%3==0:
        return 0
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return 0
    return 1


T=int(input())

n=[]
for i in range(T):
  n.append(int(input()))

for i in n:


def pan(n):
    I=0
    for i in range(n,0,-1):
        if ispr(i):
            I=i
            break
    d=n-I
    if d==
