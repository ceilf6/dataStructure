N,Q=map(int,input().split())

R=list(map(int,input().split()))

X=[]
for i in range(Q):
    X.append(int(input()))

R.sort()


summ=[]
summ.append(R[0])
for i in range(1,len(R)):
    summ.append(summ[i-1]+R[i])

import bisect

for i in range(Q):
    print(bisect.bisect_right(summ,X[i]))
