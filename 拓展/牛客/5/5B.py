import math
N=int(input())

for i in range(N):
    n,t,k=map(int,input().split())

    k2=n//(t+1)
    k3=n%(t+1)
    if k3==t:
        k2+=1
        k3=0
        #k+=1

    if k>k2+k3:
        k2=k2-math.ceil((k-k2-k3)/t)

    if k2>=0:
        print(k2)
    else:
        print('0')
