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

I=2
d=1
for i in range(3,1000):
    if ispr(i):
        print(i)
        d2=i-I
        I=i
        d=max(d2,d)

print(d)
