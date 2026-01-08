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
        ZOpack(k*c,k*w)
        m-=k
        k*=2

    ZOpack(F,m*c,m*w)

'''
while 1:
    try:
        l=list(map(int,input().split()))
        V=l[0]
        n=l[1]
        m=[0]*n
        w=[0]*n
        for i in range(n):
            m[i]=l[2+2*i]
            w[i]=l[3+2*i]
            
    except:
        break
'''
C=int(input())
for a in range(C):
    V,n=map(int,input().split())
    c=[0]*n
    w=[0]*n
    m=[0]*n
    for i in range(n):
        c[i],w[i],m[i]=map(int,input().split())
    F=[0]*(V+1)
    for i in range(n):
        Mpack(F,c[i],w[i],m[i])
    print(F[-1])
