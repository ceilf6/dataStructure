N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

x=[]
y=[]
z=[]

for i in range(N):
    x.append(A[i]-B[i]-C[i])
    y.append(B[i]-A[i]-C[i])
    z.append(C[i]-A[i]-B[i])
'''
x.sort(reverse=1)
y.sort(reverse=1)
z.sort(reverse=1)

print(x)
print(y)
print(z)
'''

sumx=sum(x)
sumy=sum(y)
sumz=sum(z)

#print(sumx,sumy,sumz)
i1=0
i2=0
i3=0

sum1=-1
sum2=-1
sum3=-1

flag1=1
flag2=1
flag3=1
x.sort(reverse=1)
y.sort(reverse=1)
z.sort(reverse=1)
#print(x,y,z)
for i in range(N):
    i1+=x[i]
    i2+=y[i]
    i3+=z[i]
    if i1>0:
        sum1=max(sum1,i+1)
        #flag1=0
    if i2>0 :
        sum2=max(sum2,i+1)
        flag2=0
    if i3>0:
        sum3=max(sum3,i+1)
        flag3=0


print(max(sum1,sum2,sum3))

