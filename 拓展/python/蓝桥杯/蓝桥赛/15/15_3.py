n=int(input())

a=list(map(int,input().split()))

b=[0]*(10**3)
b[1]=1
for i in range(2,10**3):
    b[i]=b[i-1]+i

summ=n
for i in a:
    B=0
    J=0
    for j in range(1,1000):
        if b[j]==i:
            summ-=1
            break
        elif b[j]>i:
            B=b[j]
            break
    while B>i:
        J+=1
        B-=b[J]
        if B==i:
            summ-=1
            break
print(b)
