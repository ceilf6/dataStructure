n,m=map(int,input().split())

a=list(map(int,input().split()))
'''
f=a.copy()
for i in range(m+1,n+1):
    ma=0
    for j in range(1,i//2+1):
        #分割思路错误：这样就必须是分两段
        if j>=n:
            break
        ma=max(ma,f[j-1]+f[i-j-1])
    f.append(ma)
'''

#重新理一下：空间为n固定，要求价值最大：完全背包
F=[0]*(n+1)
def Cpack(F,c,w):
    for j in range(c,n+1):
        F[j]=max(F[j],F[j-c]+w)

for i in range(1,m+1):#每天喂多少水果，也就是占用的容量
    c=i
    w=a[i-1]
    Cpack(F,c,w)

print(F[-1])
