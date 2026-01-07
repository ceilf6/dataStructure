a=list(map(int,input().split()))

K=0
K+=a[1]

n1=a[0]
nL=min(a[-4],a[-3])

if n1>nL:
    K+=3*nL
    n1-=nL
    K+=n1//2*2
else:
    K+=3*n1
    nL-=n1
    K+=nL*2

print(K)
