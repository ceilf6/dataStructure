l,r=map(int,input().split())

def ji(n):
    summ=1
    while n:
        summ*=(n%10)
        n//=10
    return summ

def chi(n):
    cnt=0
    while 1:
        n=ji(n)
        cnt+=1
        if n//10==0:
            return cnt


nmax=[]
maxx=0

for i in range(l,r):
    if chi(i)>maxx:
        maxx=chi(i)
        nmax=[i]
    elif chi(i)==maxx:
        nmax.append(i)

print(maxx)
print(*nmax)
