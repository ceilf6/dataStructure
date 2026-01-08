n,k=map(int,input().split())
l=n-k

a=list(map(int,input().split()))
maxx=0

for i in range(n-l):
    maxx=max(maxx,sum(a[i:i+l]))

if k==0:
    print(sum(a[:]))
else:print(maxx)
