n=int(input())

a=list(map(int,input().split()))

ass=sorted(a)

mu=[0]*n

for i in range(n):
    if a[i]!=ass[i]:
        mu[i]=1
#print(a,ass,mu)

from collections import Counter
d=2

import bisect as bi

lenn=0
'''
for i in range(len(mu)):
    if mu[i]==1:
        lenn=max(lenn,bi.bisect_left(mu,1,lo=i+1)-i)
'''
i=0
while i<len(mu):
    
    if mu[i]==1:
        for j in range(i+1,len(mu)):
            if mu[j]==1:
                lenn=max(lenn,j-i)
                i=j-1
                break
    i+=1
#print(lenn)
if lenn%2==0:
    print(lenn//2+1)
else:
    print((lenn+1)//2)

'''
start=bi.bisect_left(a,1)
a=a[start:]

flag=[1,1]
end=[0,1]
while flag[0] or flag[1]:
    if flag[d%2]:
        n0=mu.count(0)
        print(n0)
        if n0==n-(n//(d)):
            for i in range(d,len(a),d):
                if mu[i]==0:
                    flag[d%2]=0
                    end[d%2]=d
                    break
    d+=1

print(end[0]//2+(end[1]+1)//2)
'''
