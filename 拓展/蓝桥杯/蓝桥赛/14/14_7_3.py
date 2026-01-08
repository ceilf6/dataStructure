

n=int(input())

A=list(map(int,input().split()))
A.sort()
#print(A)
x=A.count(A[0])
m=A[0]
flag=1
while flag:
    if x%(m+1)==0:
        m+=1
        x/=m
        x+=A.count(m)
    else:
        flag=0

print(m)
