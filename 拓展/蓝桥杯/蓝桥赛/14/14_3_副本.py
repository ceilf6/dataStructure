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
i1=0
i2=0
i3=0

sum1=-1
sum2=-1
sum3=-1

for i in range(N):
    i1+=x[i]
    i2+=y[i]
    i3+=z[i]
    if i1>0:
        sum1=i+1
        break
    if i2>0:
        sum2=i+1
    if i3>0:
        sum3=i+1


if sum1!=-1:
    print(sum1)
elif sum2!=-1:
    print(sum2)
elif sum3!=-1:
    print(sum3)
else:
    print(-1)
