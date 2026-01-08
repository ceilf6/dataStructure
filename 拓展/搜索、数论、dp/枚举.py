import os
import sys

n,k=map(int,input().split())

a=list(map(int,input().split()))

a.sort()

sum2=[0]*k
for i in range(k):
  sum2[i]=(sum(a[:2*(k-i)-1])+sum(a[-i-1:]))

sum2.sort()
print(sum2[0])
