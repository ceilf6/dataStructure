def ZOpack(F,c,w):
    for j in range(V,c-1,-1):
        F[j]=max(F[j],F[j-c]+w)

def Cpack(F,c,w):  
    for j in range(c,V+1):
        F[j]=max(F[j],F[j-c]+w)

def Mpack(F,c,w,m):
    if c*m>=V:
        Cpack(F,c,w)
        return

    k=1
    while k<m:
        ZOpack(F,k*c,k*w)
        m=m-k
        k=2*k
    ZOpack(F,c*m,w*m)


n,V=map(int,input().split())
M=[0]*n
C=[0]*n
W=[0]*n
for i in range(n):
    M[i],C[i],W[i]=map(int,input().split())
F=[0]*(V+1)

for i in range(n):
    Mpack(F,C[i],W[i],M[i])
print(F[-1])
