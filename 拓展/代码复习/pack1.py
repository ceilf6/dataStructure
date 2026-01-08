def ZOpack(F,c,w):
    for j in range(V,c-1,-1):
        F[j]=max(F[j],F[j-c]+w)

def Cpack(F,c,w):
    for j in range(c,V+1):
        F[j]=max(F[j],F[j-c]+w)

def Mpack(F,c,w,m):
    if c*m >= V:
        Cpack(F,c,w)

    k=1
    while k<m:
        ZOpack(F,k*c,k*w)
        m-=k
        k*=2
    ZOpack(F,c*m,w*m)


from collections import defaultdict

group=defaultdict(list)


F=[0]*(V+1)

for i in group:
    for j in range(V,-1,-1):
        for c,w in group[i]:
            if j>=c:
                F[j]=max(
