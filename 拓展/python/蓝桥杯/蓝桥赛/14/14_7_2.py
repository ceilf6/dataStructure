import bisect
from collections import defaultdict
from collections import Counter
n=int(input())

A=list(map(int,input().split()))
'''
A.sort()

#c=defaultdict(int)
c1=[]
c2=[]
l=0
r=0
while r<len(A):
    r=bisect.bisect_right(A,A[r])

    c[A[l]][0]=A[l]
    c[A[l]][1]=r-l

    c1.append(A[l])
    c2.append(r-l)
    l=r
print(c1,c2)
'''

c=dict(Counter(A))
keys=list(c.keys())
m=keys[0]
flag=0
while 1:#not flag:#not flag:
    #print(m)#一直没出去！！！
    '''
    if flag:
        break
    '''
    summ=0
    for j in range(bisect.bisect_left(keys,m),len(keys)):
        f=1
        for z in range(m+1,keys[j]+1):
            f*=z
        summ+=f*c[keys[j]]
        #print(summ)
    if summ==0:
        print(m)
        break
    else:
        if summ%(m+1)==0:
            m+=1
        else:
            print(m)
            #flag=1
            break
    
