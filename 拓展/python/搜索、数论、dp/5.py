import math
a=list(map(int,input().split()))
n=a[0]
m=a[1]
b=[list(map(int,input().split())) for k in range(n)]
sum=0
max=0
for i in range(n):
    for j in range(m):
        for i2 in range(i+1,n):
            for j2 in range(j+1,m):
                if(i2-i==j2-j):
                    for p in range(i,i2+1):
                        sum+=b[p][j]+b[p][j2]
                    for q in range(j,j2+1):
                        sum+=b[i][q]+b[i2][q]
                    sum-=(b[i][j]+b[i][j2]+b[i2][j]+b[i2][j2])
                    if sum>max:
                        max=sum
                    sum=0
print(max)
