n=int(input())

l=list(map(int,input().split()))

from itertools import combinations

maxx=0
for i in range(n):
    su=l[i]
    j=i+1
    while j<n:
        su+=l[j]
        maxx=max(su,maxx)



print(maxx)
