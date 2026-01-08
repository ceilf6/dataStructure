
dp1=[0]*100
def dp_1(n):
    if n==1 or n==2:
        return 1
    if dp1[n]!=0:
        return dp1[n]
    dp1[n]=dp_1(n-1)+dp_1(n-2) #存储
    return dp1[n]


dp2=[0]*100
def dp_2(n):
    dp2[0]=dp2[1]=1
    for i in range(2,n):
        dp2[i]=dp2[i-1]+dp2[i-2]
    return dp2[n-1]

print(dp_1(10))
print(dp_2(10))
