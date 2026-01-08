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
        m-=k
        k*=2

    ZOpack(F,m*c,m*w)



for k in group:
    for j in range(V,-1,-1):
        for c,w in group[k]:
            if j>=c:
                F[j]=max(F[j],F[j-c]+w)
