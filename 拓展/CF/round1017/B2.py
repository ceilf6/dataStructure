t=int(input())
import math
for i in range(t):
    n,m,l,r=map(int,input().split())
    print(math.floor(m/n*l),math.floor(m/n*r))
