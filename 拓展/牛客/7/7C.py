N=int(input())
import math
a=list(map(int,input().split()))

summ=0
while sum(1 for i in a if i>0)>0:
    summ+=1

    for j in range(N):
        a[j]=max(a[j]-1,0)
        #print(j)

    a.sort(reverse=1)

    a[0]=max(a[0]-1,0)

    #print(a)
    a.sort(reverse=1)

    a[0],a[1]=max(a[0]-1,0),max(a[1]-1,0)
    '''
    print(a)
    print('summ',summ)
    '''
print(summ)
