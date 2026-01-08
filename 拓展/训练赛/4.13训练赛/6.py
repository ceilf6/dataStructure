n=int(input())

sum1=0
sum2=0
'''
for i in range(1,1+n+1):
    sum1+=i**2
for i in range(1+n+1,1+2*n+1):
    sum2+=i**2

now=1
while sum1!=sum2:
    sum1-=now**2
    sum1+=(now+n+1)**2
    sum2-=(now+n+1)**2
    sum2+=(now+n*2+1)**2
    now+=1
'''
now=n*(2*n+1)
for i in range(n):
    print(f"{now+i}^2 + ",end='')
print(f"{now+n}^2 =")

for i in range(n-1):
    print(f"{now+n+1+i}^2 + ",end='')
print(f"{now+2*n}^2",end='')
