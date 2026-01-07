from math import sqrt
T=int(input())

n=[]

for i in range(T):
    n.append(int(input()))

nmax=max(n)

zhi=[]

for i in range(2,nmax+1):
    flag=1
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            flag=0
            break
    if flag:
        zhi.append(i)

#print(zhi)

dp=[0]*(nmax+1)

#print(dp)


for i in range(2,nmax+1):
    zhii=-1
    dp[i]=0
    while zhii+1<=len(zhi)-1:
        #print(zhii)
        zhii+=1
        if zhi[zhii]<=i:#已经加过1了呀！！  
        #print(i,zhi[zhii])
            if dp[i-zhi[zhii]]==0: #说明小蓝选a[j]这个质数留给小桥的是必输的局面，小蓝赢
                dp[i]=1
                break
#print(dp)


for i in n:
    print(dp[i])
